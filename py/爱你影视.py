#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import re
from urllib.parse import quote, unquote
import time

class Spider:
    def init(self, extend=""):
        pass
    def getName(self):
        return ""
    def homeContent(self, filter):
        return {}
    def homeVideoContent(self):
        return {}
    def categoryContent(self, tid, pg, filter, extend):
        return {}
    def detailContent(self, ids):
        return {}
    def playerContent(self, flag, id, flags):
        return {}
    def searchContent(self, key, quick):
        return {}
    def isVideoFormat(self, url):
        pass
    def manualVideoCheck(self):
        pass

class AiniVod(Spider):
    def getName(self):
        return "爱你影视"

    def init(self, extend=""):
        self.host = "https://ainivod.com"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Mobile) AppleWebKit/537.36',
            'Referer': self.host
        }
        print("爱你影视初始化完成")

    def homeContent(self, filter):
        result = {}
        try:
            # 分类数据
            classes = [
                {"type_id": "1", "type_name": "电影"},
                {"type_id": "2", "type_name": "连续剧"},
                {"type_id": "4", "type_name": "动漫"},
                {"type_id": "20", "type_name": "短剧"},
                {"type_id": "3", "type_name": "综艺"},
                {"type_id": "43", "type_name": "记录片"}
            ]

            # 获取首页数据
            r = requests.get(self.host, headers=self.headers, timeout=10)
            r.encoding = 'utf-8'
            html = r.text

            # 解析推荐视频
            vods = []
            # 匹配视频项
            pattern = r'<a class="hl-item-thumb[^>]*href="/voddetail/(\d+)\.html"[^>]*data-original="([^"]*)"[^>]*>.*?<div class="hl-item-title[^>]*">.*?<a[^>]*>([^<]*)</a>'
            matches = re.findall(pattern, html, re.S)
            
            for match in matches[:15]:  # 取前15个
                vod_id, pic, name = match
                vods.append({
                    "vod_id": vod_id,
                    "vod_name": name.strip(),
                    "vod_pic": pic,
                    "vod_remarks": ""
                })

            result['class'] = classes
            if vods:
                result['list'] = [{
                    "vod_id": "hot",
                    "vod_name": "热播推荐", 
                    "vod_list": vods
                }]
                
        except Exception as e:
            print(f"首页错误: {e}")
            # 返回默认数据避免崩溃
            result = {
                'class': [
                    {"type_id": "1", "type_name": "电影"},
                    {"type_id": "2", "type_name": "连续剧"}
                ],
                'list': []
            }
            
        return result

    def homeVideoContent(self):
        # 首页推荐视频，可以调用homeContent或单独实现
        return self.homeContent({})

    def categoryContent(self, tid, pg, filter, extend):
        result = {}
        try:
            url = f"{self.host}/vodshow/{tid}----------{pg}---.html"
            print(f"分类请求: {url}")
            
            r = requests.get(url, headers=self.headers, timeout=10)
            r.encoding = 'utf-8'
            html = r.text

            vods = []
            # 匹配视频项，包含备注信息
            pattern = r'<a class="hl-item-thumb[^>]*href="/voddetail/(\d+)\.html"[^>]*data-original="([^"]*)"[^>]*>.*?<div class="hl-item-title[^>]*">.*?<a[^>]*>([^<]*)</a>.*?<span class="[^"]*remarks[^"]*">([^<]*)</span>'
            matches = re.findall(pattern, html, re.S)
            
            for match in matches:
                vod_id, pic, name, remarks = match
                vods.append({
                    "vod_id": vod_id,
                    "vod_name": name.strip(),
                    "vod_pic": pic,
                    "vod_remarks": remarks.strip()
                })

            result['list'] = vods
            result['page'] = int(pg)
            result['pagecount'] = 999
            result['limit'] = 20
            result['total'] = len(vods)
            
        except Exception as e:
            print(f"分类错误: {e}")
            result = {
                'list': [],
                'page': 1,
                'pagecount': 1,
                'limit': 20,
                'total': 0
            }
            
        return result

    def detailContent(self, ids):
        result = {}
        try:
            vid = ids[0]
            url = f"{self.host}/voddetail/{vid}.html"
            print(f"详情请求: {url}")
            
            r = requests.get(url, headers=self.headers, timeout=10)
            r.encoding = 'utf-8'
            html = r.text

            # 解析标题
            title_match = re.search(r'<h2 class="hl-dc-title[^>]*>([^<]*)</h2>', html)
            title = title_match.group(1).strip() if title_match else "未知标题"

            # 解析图片
            pic_match = re.search(r'data-original="([^"]*)"', html)
            pic = pic_match.group(1) if pic_match else ""

            # 解析详情信息
            director = ""
            actor = ""
            area = ""
            year = ""
            desc = ""
            remarks = ""

            # 解析详细信息
            info_matches = re.findall(r'<li[^>]*><em[^>]*>([^<]*)</em>([^<]*)</li>', html)
            for key, value in info_matches:
                key = key.strip().replace('：', '').replace(':', '')
                value = value.strip()
                if '导演' in key:
                    director = value
                elif '主演' in key:
                    actor = value
                elif '地区' in key:
                    area = value
                elif '年份' in key:
                    year = value
                elif '简介' in key:
                    desc = value
                elif '状态' in key:
                    remarks = value

            # 解析播放源
            play_from = []
            play_url = []
            
            # 查找播放源
            source_pattern = r'<a class="hl-tabs-btn[^>]*>([^<]*)</a>'
            source_matches = re.findall(source_pattern, html)
            
            for source in source_matches:
                play_from.append(source.strip())
                # 简化处理，实际需要根据页面结构解析剧集
                play_url.append(f"第1集${self.host}/vodplay/{vid}-1-1.html")

            detail = {
                "vod_id": vid,
                "vod_name": title,
                "vod_pic": pic,
                "type_name": "",
                "vod_year": year,
                "vod_area": area,
                "vod_remarks": remarks,
                "vod_actor": actor,
                "vod_director": director,
                "vod_content": desc,
                "vod_play_from": "$$$".join(play_from) if play_from else "",
                "vod_play_url": "$$$".join(play_url) if play_url else ""
            }

            result['list'] = [detail]
            
        except Exception as e:
            print(f"详情错误: {e}")
            result = {'list': []}
            
        return result

    def searchContent(self, key, quick):
        result = {}
        try:
            url = f"{self.host}/vodsearch/{quote(key)}-------------.html"
            print(f"搜索请求: {url}")
            
            r = requests.get(url, headers=self.headers, timeout=10)
            r.encoding = 'utf-8'
            html = r.text

            vods = []
            # 搜索结果的匹配模式
            pattern = r'<a class="hl-item-thumb[^>]*href="/voddetail/(\d+)\.html"[^>]*data-original="([^"]*)"[^>]*>.*?<div class="hl-item-title[^>]*">.*?<a[^>]*>([^<]*)</a>.*?<span class="[^"]*remarks[^"]*">([^<]*)</span>'
            matches = re.findall(pattern, html, re.S)
            
            for match in matches:
                vod_id, pic, name, remarks = match
                vods.append({
                    "vod_id": vod_id,
                    "vod_name": name.strip(),
                    "vod_pic": pic,
                    "vod_remarks": remarks.strip()
                })

            result['list'] = vods
            
        except Exception as e:
            print(f"搜索错误: {e}")
            result = {'list': []}
            
        return result

    def playerContent(self, flag, id, flags):
        result = {}
        try:
            # 直接返回播放地址，让TVBox的解析器处理
            result["parse"] = 0
            result["playUrl"] = ""
            result["url"] = id
            result["header"] = {
                "User-Agent": "Mozilla/5.0 (Linux; Android 10; Mobile) AppleWebKit/537.36",
                "Referer": self.host
            }
        except Exception as e:
            print(f"播放错误: {e}")
        return result

    def isVideoFormat(self, url):
        # 判断是否为视频格式
        video_formats = ['.m3u8', '.mp4', '.flv', '.avi', '.mkv']
        return any(fmt in url.lower() for fmt in video_formats)

    def manualVideoCheck(self):
        # 手动视频检查
        pass

    def localProxy(self, param):
        # 本地代理
        return None

# 创建实例
spider = AiniVod()

# TVBox 标准接口函数
def init():
    spider.init()
    return spider

def homeContent(filter):
    return spider.homeContent(filter)

def homeVideoContent():
    return spider.homeVideoContent()

def categoryContent(tid, pg, filter, extend):
    return spider.categoryContent(tid, pg, filter, extend)

def detailContent(ids):
    return spider.detailContent(ids)

def searchContent(key, quick):
    return spider.searchContent(key, quick)

def playerContent(flag, id, flags):
    return spider.playerContent(flag, id, flags)

# 本地测试
if __name__ == "__main__":
    spider.init()
    
    # 测试首页
    print("=== 测试首页 ===")
    home_data = spider.homeContent({})
    print(f"分类数量: {len(home_data.get('class', []))}")
    print(f"推荐列表: {len(home_data.get('list', []))}")
    
    # 测试搜索
    print("\n=== 测试搜索 ===")
    search_data = spider.searchContent("测试", False)
    print(f"搜索结果: {len(search_data.get('list', []))}")