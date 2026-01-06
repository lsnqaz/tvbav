# -*- coding: utf-8 -*-
# 本资源来源于互联网公开渠道，仅可用于个人学习爬虫技术。
# 严禁将其用于任何商业用途，下载后请于 24 小时内删除，搜索结果均来自源站，本人不承担任何责任。

import sys, urllib3, json
sys.path.append('..')
from base.spider import Spider
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class Spider(Spider):
    headers, host = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'X-Requested-With': 'com.hiker.youtoo',
        'Referer': 'https://film.symx.club/'
    }, 'https://film.symx.club'

    def init(self, extend=''):
        try:
            host = extend.strip().rstrip('/')
            if host.startswith('http'):
                self.host = host
                self.headers['Referer'] = host + '/'
                return None
            return None
        except Exception as e:
            print(f'初始化异常：{e}')
            return None

    def homeContent(self, filter):
        """首页分类 - 保持原版不变"""
        try:
            # 原版使用的是 /api/category/top，但抓包显示没有这个API
            # 使用正确的API获取分类
            response = self.fetch(f'{self.host}/api/film/category', headers=self.headers, verify=False)
            if response.status_code != 200:
                return {'class': []}
            
            data = response.json()
            if data.get('code') != 200:
                return {'class': []}
            
            categories = []
            seen = set()
            
            for category in data.get('data', []):
                category_id = str(category.get('categoryId', ''))
                category_name = category.get('categoryName', '')
                
                if category_id and category_id not in seen:
                    seen.add(category_id)
                    categories.append({
                        'type_id': category_id,
                        'type_name': category_name
                    })
            
            # 确保至少有基本分类
            if not categories:
                categories = [
                    {'type_id': '1', 'type_name': '电视剧'},
                    {'type_id': '2', 'type_name': '电影'},
                    {'type_id': '3', 'type_name': '综艺'},
                    {'type_id': '4', 'type_name': '动漫'},
                    {'type_id': '5', 'type_name': '短剧'}
                ]
            
            return {'class': categories}
        except Exception as e:
            print(f'首页分类异常：{e}')
            return {'class': []}

    def homeVideoContent(self):
        """首页推荐视频 - 保持原版不变"""
        try:
            response = self.fetch(f'{self.host}/api/film/category', headers=self.headers, verify=False)
            
            videos = []
            if response.status_code == 200:
                data = response.json()
                if data.get('code') == 200:
                    for category in data.get('data', []):
                        for film in category.get('filmList', [])[:10]:  # 每个分类取前10个
                            videos.append({
                                'vod_id': film.get('id'),
                                'vod_name': film.get('name'),
                                'vod_pic': film.get('cover') or film.get('poster', ''),
                                'vod_remarks': film.get('updateStatus', '')
                            })
            
            # 如果为空，尝试获取海报数据
            if not videos:
                try:
                    response = self.fetch(f'{self.host}/api/poster/list', headers=self.headers, verify=False)
                    if response.status_code == 200:
                        data = response.json()
                        if data.get('code') == 200:
                            for poster in data.get('data', []):
                                videos.append({
                                    'vod_id': poster.get('filmId'),
                                    'vod_name': poster.get('filmName'),
                                    'vod_pic': poster.get('poster'),
                                    'vod_remarks': poster.get('blurb', '')[:50] if poster.get('blurb') else ''
                                })
                except:
                    pass
            
            return {'list': videos}
        except Exception as e:
            print(f'首页视频异常：{e}')
            return {'list': []}

    def categoryContent(self, tid, pg, filter, extend):
        """分类内容 - 使用原版的API"""
        try:
            # 使用原版的API和参数格式
            url = f'{self.host}/api/film/category/list'
            params = {
                'area': '',
                'categoryId': tid,
                'language': '',
                'pageNum': str(pg),
                'pageSize': '15',
                'sort': 'updateTime',
                'year': ''
            }
            
            response = self.fetch(url, params=params, headers=self.headers, verify=False)
            
            videos = []
            if response.status_code == 200:
                data = response.json()
                if data.get('code') == 200:
                    for film in data.get('data', {}).get('list', []):
                        videos.append({
                            'vod_id': film.get('id'),
                            'vod_name': film.get('name'),
                            'vod_pic': film.get('cover'),
                            'vod_remarks': film.get('updateStatus', '')
                        })
            
            return {'list': videos, 'page': pg}
        except Exception as e:
            print(f'分类内容异常：{e}')
            return {'list': [], 'page': pg}

    def searchContent(self, key, quick, pg='1'):
        """搜索内容 - 保持原版不变"""
        try:
            response = self.fetch(f'{self.host}/api/film/search?keyword={key}&pageNum={pg}&pageSize=10', 
                                 headers=self.headers, verify=False)
            
            videos = []
            if response.status_code == 200:
                data = response.json()
                if data.get('code') == 200:
                    for film in data.get('data', {}).get('list', []):
                        videos.append({
                            'vod_id': film.get('id'),
                            'vod_name': film.get('name'),
                            'vod_pic': film.get('cover'),
                            'vod_remarks': film.get('updateStatus', ''),
                            'vod_year': film.get('year', ''),
                            'vod_area': film.get('area', ''),
                            'vod_director': film.get('director', '')
                        })
            
            return {'list': videos, 'page': pg}
        except Exception as e:
            print(f'搜索异常：{e}')
            return {'list': [], 'page': pg}

    def detailContent(self, ids):
        """详情内容 - 保持原版不变"""
        try:
            response = self.fetch(f'{self.host}/api/film/detail?id={ids[0]}', headers=self.headers, verify=False)
            
            if response.status_code != 200:
                return {'list': []}
            
            data = response.json()
            if data.get('code') != 200:
                return {'list': []}
            
            film_data = data['data']
            video, show, play_urls = {}, [], []
            
            # 解析播放线路 - 关键部分保持原版
            for play_line in film_data['playLineList']:
                show.append(play_line['playerName'])
                play_url = []
                for line in play_line['lines']:
                    play_url.append(f"{line['name']}${line['id']}")
                play_urls.append('#'.join(play_url))
            
            # 构建视频信息
            video.update({
                'vod_id': film_data.get('id'),
                'vod_name': film_data.get('name'),
                'vod_pic': film_data.get('cover'),
                'vod_year': film_data.get('year'),
                'vod_area': film_data.get('other'),  # 注意：原版使用'other'字段
                'vod_actor': film_data.get('actor'),
                'vod_director': film_data.get('director'),
                'vod_content': film_data.get('blurb'),
                'vod_score': film_data.get('doubanScore'),
                'vod_play_from': '$$$'.join(show),
                'vod_play_url': '$$$'.join(play_urls)
            })
            
            return {'list': [video]}
        except Exception as e:
            print(f'详情异常：{e}')
            return {'list': []}

    def playerContent(self, flag, id, vipflags):
        """播放地址 - 保持原版不变"""
        try:
            response = self.fetch(f'{self.host}/api/line/play/parse?lineId={id}', headers=self.headers)
            
            if response.status_code != 200:
                return {'jx': '0', 'parse': '0', 'url': '', 'header': {}}
            
            data = response.json()
            if data.get('code') != 200:
                return {'jx': '0', 'parse': '0', 'url': '', 'header': {}}
            
            play_url = data.get('data', '')
            
            return {
                'jx': '0',
                'parse': '0',
                'url': play_url,
                'header': {
                    'User-Agent': self.headers['User-Agent'],
                    'Referer': self.host + '/'
                }
            }
        except Exception as e:
            print(f'播放地址异常：{e}')
            return {'jx': '0', 'parse': '0', 'url': '', 'header': {}}

    def getName(self):
        """返回爬虫名称"""
        return "木兮影视"

    def isVideoFormat(self, url):
        """判断是否为视频格式"""
        pass

    def manualVideoCheck(self):
        """手动视频检查"""
        pass

    def destroy(self):
        """清理资源"""
        pass

    def localProxy(self, param):
        """本地代理"""
        pass