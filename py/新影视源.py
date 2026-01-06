# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
from base.spider import Spider

class Spider(Spider):

    def init(self, extend=""):
        pass

    def isVideoFormat(self, url):
        pass

    def manualVideoCheck(self):
        pass

    def destroy(self):
        pass

    host = 'http://194.147.100.13'
    
    headers = {
        "User-Agent": "okhttp/3.12.11"
    }

    def homeContent(self, filter):
        data = self.fetch(f"{self.host}/api.php/v2.vod/androidtypes", headers=self.headers).json()
        dy = {
            "classes": "类型",
            "areas": "地区", 
            "years": "年份",
            "sortby": "排序",
        }
        filters = {}
        classes = []
        for item in data['data']:
            has_non_empty_field = False
            item['sortby'] = ['updatetime', 'hits', 'score']
            demos = ['时间', '人气', '评分']
            classes.append({"type_name": item["type_name"], "type_id": str(item["type_id"])})
            for key in dy:
                if key in item and len(item[key]) > 1:
                    has_non_empty_field = True
                    break
            if has_non_empty_field:
                filters[str(item["type_id"])] = []
                for dkey in item:
                    if dkey in dy and len(item[dkey]) > 1:
                        values = item[dkey]
                        value_array = [
                            {"n": demos[idx] if dkey == "sortby" else value.strip(), "v": value.strip()}
                            for idx, value in enumerate(values)
                            if value.strip() != ""
                        ]
                        filters[str(item["type_id"])].append(
                            {"key": dkey, "name": dy[dkey], "value": value_array}
                        )
        result = {}
        result["class"] = classes
        result["filters"] = filters
        return result

    def homeVideoContent(self):
        rsp = self.fetch(f"{self.host}/api.php/v2.vod/androidhome", headers=self.headers).json()
        videos = []
        for i in rsp['data']['list']:
            videos.extend(self.getlist(i['list']))
        return {'list': videos}

    def categoryContent(self, tid, pg, filter, extend):
        params = {
            "page": pg,
            "type": tid,
            "area": extend.get('areas',''),
            "year": extend.get('years',''), 
            "sortby": extend.get('sortby',''),
            "class": extend.get('classes','')
        }
        params = {i: v for i, v in params.items() if v}
        rsp = self.fetch(f'{self.host}/api.php/v2.vod/androidlist', headers=self.headers, params=params).json()
        result = {}
        result['list'] = self.getlist(rsp['data'])
        result['page'] = pg
        result['pagecount'] = 9999
        result['limit'] = 90
        result['total'] = 999999
        return result

    def detailContent(self, ids):
        rsp = self.fetch(f'{self.host}/api.php/v2.vod/androiddetail?vod_id={ids[0]}', headers=self.headers).json()
        v = rsp['data']
        vod = {
            'vod_id': v['id'],
            'vod_name': v['name'],
            'vod_pic': v['pic'],
            'vod_year': v.get('year'),
            'vod_area': v.get('area'),
            'vod_remarks': v.get('remarks'),
            'vod_actor': v.get('actor'),
            'vod_director': v.get('director'),
            'vod_content': v.get('content'),
            'vod_play_from': '新影视源',
            'vod_play_url': '#'.join([f"{i['player']}${i['url']}" for i in v['urls']])
        }
        return {'list': [vod]}

    def searchContent(self, key, quick, pg='1'):
        rsp = self.fetch(f'{self.host}/api.php/v2.vod/androidsearch?page={pg}&wd={key}', headers=self.headers).json()
        return {'list': self.getlist(rsp['data']), 'page': pg}

    def playerContent(self, flag, id, vipFlags):
        return {"parse": 0, "url": id}

    def localProxy(self, param):
        pass

    def getlist(self, data):
        videos = []
        for vod in data:
            videos.append({
                "vod_id": vod['id'],
                "vod_name": vod['name'],
                "vod_pic": vod['pic'],
                "vod_remarks": vod.get('remarks', '')
            })
        return videos