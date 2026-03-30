# -*- coding: utf-8 -*-
# by @嗷呜
# 基于原作者 @嗷呜 版本修改，仅可用于个人学习用途

from base.spider import Spider
import re
import sys
import requests

sys.path.append('..')

class Spider(Spider):
    def getName(self):
        return "央视卫视+港澳电影电视直播"
    
    def init(self, extend):
        pass
    
    def isVideoFormat(self, url):
        # 检查是否是视频格式
        return any(url.endswith(ext) for ext in ['.m3u8', '.mp4', '.flv', '.avi', '.mkv', '.mov'])
    
    def manualVideoCheck(self):
        return False

    def homeContent(self, filter):
        result = {
            "class": [
                {"type_id": "gangaodianying", "type_name": "央视卫视+港澳电影电视直播"}
            ]
        }
        return result

    def homeVideoContent(self):
        return {'list': []}

    def categoryContent(self, tid, pg, filter, extend):
        # 只有一个分类
        if tid == "gangaodianying":
            # 显示六个条目：电视直播、电影直播、港澳电视直播、直播合体、ZBDS、TV1288
            items = [
                {
                    "vod_id": "tv_live",
                    "vod_name": "电视直播",
                    "vod_pic": "https://d.kstore.dev/download/13922/my/1770993716831_edit_1000034077972.png",
                    "vod_remarks": "央视+卫视 共54个频道"
                },
                {
                    "vod_id": "movie_live",
                    "vod_name": "电影直播",
                    "vod_pic": "https://d.kstore.dev/download/13922/my/1770184570454_edit_81178439473549.png",
                    "vod_remarks": "19个电影频道"
                },
                {
                    "vod_id": "hk_live",
                    "vod_name": "港澳电视直播",
                    "vod_pic": "https://d.kstore.dev/download/13922/my/1770183848454_edit_80429983213246.png",
                    "vod_remarks": "40个港澳频道"
                },
                {
                    "vod_id": "hk_main",
                    "vod_name": "直播合体",
                    "vod_pic": "https://d.kstore.dev/download/13922/my/Screenshot_20260214_074021_com.larus.nova_edit_11339134734206.jpg",
                    "vod_remarks": "从网络M3U获取的最新频道"
                },
                {
                    "vod_id": "zbds",
                    "vod_name": "ZBDS",
                    "vod_pic": "https://d.kstore.dev/download/13922/my/1771027192080_edit_12441842540288.png",
                    "vod_remarks": "从ZBDS TXT获取的最新频道"
                },
                {
                    "vod_id": "tv1288",
                    "vod_name": "TV1288",
                    "vod_pic": "https://d.kstore.dev/download/13922/my/1773896168399_edit_23497488165164.png",
                    "vod_remarks": "从TV1288 M3U获取的最新频道"
                }
            ]
            return {
                'list': items,
                'page': 1,
                'pagecount': 1,
                'limit': 18,
                'total': 6  # 总数更新为6
            }
        
        return {'list': []}

    def detailContent(self, ids):
        vod_id = ids[0]
        
        # 电视直播详情
        if vod_id == "tv_live":
            # 央视+卫视频道列表 - 使用$分隔符，与电影和港澳频道格式一致
            tv_channels = [
                "CCTV1综合$http://113.26.251.182:8009/hls/1/index.m3u8",
                "CCTV2财经$http://113.26.251.182:8009/hls/2/index.m3u8",
                "CCTV3综艺$http://113.26.251.182:8009/hls/3/index.m3u8",
                "CCTV4中文国际$http://113.26.251.182:8009/hls/4/index.m3u8",
                "CCTV5体育$http://113.26.251.182:8009/hls/5/index.m3u8",
                "CCTV5+体育赛事$http://113.26.251.182:8009/hls/18/index.m3u8",
                "CCTV6电影$http://113.26.251.182:8009/hls/6/index.m3u8",
                "CCTV7国防军事$http://113.26.251.182:8009/hls/7/index.m3u8",
                "CCTV8电视剧$http://113.26.251.182:8009/hls/8/index.m3u8",
                "CCTV9纪录$http://113.26.251.182:8009/hls/9/index.m3u8",
                "CCTV10科教$http://113.26.251.182:8009/hls/10/index.m3u8",
                "CCTV11戏曲$http://113.26.251.182:8009/hls/11/index.m3u8",
                "CCTV12社会与法$http://113.26.251.182:8009/hls/12/index.m3u8",
                "CCTV13新闻$http://113.26.251.182:8009/hls/13/index.m3u8",
                "CCTV14少儿$http://113.26.251.182:8009/hls/14/index.m3u8",
                "CCTV15音乐$http://113.26.251.182:8009/hls/15/index.m3u8",
                "CCTV17农业农村$http://113.26.251.182:8009/hls/17/index.m3u8",
                "北京卫视$http://113.26.251.182:8009/hls/30/index.m3u8",
                "天津卫视$http://113.26.251.182:8009/hls/40/index.m3u8",
                "东方卫视$http://113.26.251.182:8009/hls/29/index.m3u8",
                "东南卫视$http://113.26.251.182:8009/hls/57/index.m3u8",
                "广东卫视$http://113.26.251.182:8009/hls/48/index.m3u8",
                "广西卫视$http://113.26.251.182:8009/hls/36/index.m3u8",
                "深圳卫视$http://113.26.251.182:8009/hls/42/index.m3u8",
                "江苏卫视$http://113.26.251.182:8009/hls/34/index.m3u8",
                "江西卫视$http://113.26.251.182:8009/hls/49/index.m3u8",
                "浙江卫视$http://113.26.251.182:8009/hls/35/index.m3u8",
                "湖南卫视$http://113.26.251.182:8009/hls/31/index.m3u8",
                "湖北卫视$http://113.26.251.182:8009/hls/39/index.m3u8",
                "安徽卫视$http://113.26.251.182:8009/hls/50/index.m3u8",
                "山东卫视$http://113.26.251.182:8009/hls/41/index.m3u8",
                "山西卫视$http://113.26.251.182:8009/hls/19/index.m3u8",
                "教育卫视$http://113.26.251.182:8009/hls/65/index.m3u8",
                "河北卫视$http://113.26.251.182:8009/hls/45/index.m3u8",
                "龙江卫视$http://113.26.251.182:8009/hls/44/index.m3u8",
                "吉林卫视$http://113.26.251.182:8009/hls/46/index.m3u8",
                "辽宁卫视$http://113.26.251.182:8009/hls/43/index.m3u8",
                "云南卫视$http://113.26.251.182:8009/hls/33/index.m3u8",
                "贵州卫视$http://113.26.251.182:8009/hls/37/index.m3u8",
                "四川卫视$http://113.26.251.182:8009/hls/38/index.m3u8",
                "重庆卫视$http://113.26.251.182:8009/hls/32/index.m3u8",
                "甘肃卫视$http://113.26.251.182:8009/hls/51/index.m3u8",
                "宁夏卫视$http://113.26.251.182:8009/hls/52/index.m3u8",
                "青海卫视$http://113.26.251.182:8009/hls/53/index.m3u8",
                "内蒙卫视$http://113.26.251.182:8009/hls/47/index.m3u8",
                "西藏卫视$http://113.26.251.182:8009/hls/54/index.m3u8",
                "新疆卫视$http://113.26.251.182:8009/hls/55/index.m3u8",
                "卡酷少儿$http://113.26.251.182:8009/hls/61/index.m3u8",
                "优漫卡通$http://113.26.251.182:8009/hls/60/index.m3u8",
                "广东珠江$http://r.jdshipin.com/sE5vO",
                "广东珠江备用$http://php.jdshipin.com/TVOD/iptv.php?id=gdzj",
                "广东体育$http://r.jdshipin.com/LiYdg"
            ]
            
            vod_info = {
                "vod_id": "tv_live",
                "vod_name": "电视直播",
                "vod_pic": "https://d.kstore.dev/download/13922/my/1770993716831_edit_1000034077972.png",
                "vod_remarks": "央视+卫视 共54个频道",
                "vod_content": "包含CCTV1-17、北京卫视、东方卫视、湖南卫视、浙江卫视、江苏卫视、广东卫视等央视及卫视频道",
                "vod_play_from": "央视卫视",
                "vod_play_url": "#".join(tv_channels)
            }
            
            return {'list': [vod_info]}
        
        # 电影直播详情
        elif vod_id == "movie_live":
            # 电影直播频道列表
            movie_channels = [
                "NOW爆谷$http://208.87.242.79/livehttpplay?channel_id=13002",
                "NOW星影$http://208.87.242.79/livehttpplay?channel_id=13003",
                "天映经典$https://cdn9.163189.xyz/smt1.1.php?id=Celestial2",
                "邵氏动作$http://38.75.136.137:98/gslb/dsdqpub/lbssdz.m3u8?auth=testpub",
                "邵氏喜剧$http://38.75.136.137:98/gslb/dsdqpub/lbssxj.m3u8?auth=testpub",
                "邵氏电影$http://38.75.136.137:98/gslb/dsdqpub/lbssdy.m3u8?auth=testpub",
                "邵氏武侠$http://38.75.136.137:98/gslb/dsdqpub/lbsswx.m3u8?auth=testpub",
                "Astr爱奇艺1$https://smt.1678520.xyz/smt3.2.1.php?id=Qiyi",
                "Astr爱奇艺2$http://php.jdshipin.com:8880/smt.php?id=Qiyi",
                "Astr爱奇艺3$https://o11.163189.xyz/stream/live/iqiyi/",
                "华数电影$http://hmfs.f3322.net:3388/hls/40/index.m3u8",
                "CHC家庭影院$http://38.75.136.137:98/gslb/dsdqpub/chcjt.m3u8?auth=testpub",
                "CHC动作电影$http://38.75.136.137:98/gslb/dsdqpub/chcdz.m3u8?auth=testpub",
                "CHC影迷电影$http://38.75.136.137:98/gslb/dsdqpub/chchd.m3u8?auth=testpub",
                "Y+剧场$http://hms3659nc3747353871.live.aikan.miguvideo.com/PLTV/88888888/224/3221230226/1.m3u8?tenantId=8601&accountinfo=~~V2.0~SSxnh2gPZaV_9wZMz86ofwc38bf04ecfc078f584095a9c6e91b9e1~3twbaBwUaqzfkJ5qW9C0gp1C11OJXhanim-P8XrfoHFX-jV3R0FL2wbo-VR8pOhzd5938d01ed8f640cebb709a281e7b1d3~ExtInfo9W1qynAo8QtSBzK-JlHBbQ3bb1f3410d135b117fdf58086980a86d:20240603131532:UTC,c864060416ccf5986b3e5940417477879245774,117.148.130.144,20240603131532,4444444684,c864060416ccf5986b3e5940417477879245774,-1,0,1,,,2,1000000201,,,2,23,0,241,9ec0a2dcdcfd4259318d50a38cde552c,,,1,1,140151867,END&fbl=",
                "龙华电影$https://cdn8.163189.xyz/163189/lhdy",
                "龙华电影备用$http://cdn8.163189.xyz/163189/lhdy"
            ]
            
            vod_info = {
                "vod_id": "movie_live",
                "vod_name": "电影直播",
                "vod_pic": "https://d.kstore.dev/download/13922/my/1770184570454_edit_81178439473549.png",
                "vod_remarks": "19个电影直播频道",
                "vod_content": "包含爱奇艺、华数电影、CHC系列、Y+剧场、天映、邵氏、龙华电影、NOW爆谷、NOW星影等电影频道",
                "vod_play_from": "电影频道",
                "vod_play_url": "#".join(movie_channels)
            }
            
            return {'list': [vod_info]}
        
        # 港澳电视直播详情
        elif vod_id == "hk_live":
            # 港澳直播频道列表
            hk_channels = [
                "翡翠台字幕$http://mytv.cdn.loc.cc/o12.php?id=fct",
                "翡翠台$http://r.jdshipin.com/qrfbg",
                "明珠台字幕$http://mytv.cdn.loc.cc/o12.php?id=mzt",
                "明珠台(多音轨字幕)$https://o11.163189.xyz/stream/tvb/mzt/",
                "华丽翡翠台(多音轨字幕)$https://o11.163189.xyz/stream/live/hlt/",
                "华丽翡翠台(新加坡)$https://o11.163189.xyz/stream/live/jade/",
                "翡翠台4K(多音轨字幕)$https://o11.163189.xyz/stream/tvb/fct4k/",
                "翡翠台(多音轨字幕)$https://o11.163189.xyz/stream/tvb/fct/",
                "TVB PLUS(多音轨字幕)$https://o11.163189.xyz/stream/tvb/tvbp/",
                "Astro AOD(多音轨字幕)$https://o11.163189.xyz/stream/live/aod/",
                "Astro AEC(多音轨字幕)$https://o11.163189.xyz/stream/live/aec/",
                "TVB星河(多音轨字幕)$https://o11.163189.xyz/stream/live/tvbxh/",
                "TVB星河备用$http://r.jdshipin.com/Voac4",
                "千禧经典台$https://o11.163189.xyz/stream/live/tvbc/",
                "星光怀旧台$http://data.3g.yy.com/live/hls/1354936134/1354936134.m3u8",
                "香港卫视$http://webcast.hkstv.tv/livestream/mutfysrq/playlist.m3u8",
                "亚洲卫视$https://p2hs.vzan.com/slowlive/821481626725612419/live.m3u8",
                "有线新闻Mttv$http://hls.168.us.kg/u/78/master.m3u8",
                "无线新闻Mttv$http://hls.168.us.kg/u/83/master.m3u8",
                "Now新闻Mttv$http://hls.168.us.kg/u/332/master.m3u8",
                "无线翡翠Mttv$http://hls.168.us.kg/u/81/master.m3u8",
                "无线明珠Mttv$http://hls.168.us.kg/u/84/master.m3u8",
                "有线赛讯Mttv$http://hls.168.us.kg/u/76/master.m3u8",
                "有线综合Mttv$http://hls.168.us.kg/u/77/master.m3u8",
                "Plus综合Mttv$http://hls.168.us.kg/u/82/master.m3u8",
                "Now财经Mttv$http://hls.168.us.kg/u/333/master.m3u8",
                "Now直播Mttv$http://hls.168.us.kg/u/331/master.m3u8",
                "Now体育Mttv$http://hls.168.us.kg/u/630/master.m3u8",
                "VIUTV'粤Mttv$http://hls.168.us.kg/u/99/master.m3u8",
                "VIUTV'英Mttv$http://hls.168.us.kg/u/96/master.m3u8",
                "RTHK-31Mttv$http://hls.168.us.kg/u/31/master.m3u8",
                "澳门资讯$http://103.233.191.134:1935/ch5/info_ch5.live/playlist.m3u8",
                "澳门澳视$http://103.233.191.134:1935/ch1/ch1.live/playlist.m3u8",
                "澳门综艺$http://103.233.191.134:1935/ch6/hd_ch6.live/playlist.m3u8",
                "龙华偶像$https://cdn8.163189.xyz/163189/lhox",
                "龙华偶像备用$http://cdn8.163189.xyz/163189/lhox",
                "龙华戏剧$https://cdn8.163189.xyz/163189/lhxj",
                "龙华戏剧备用$http://cdn8.163189.xyz/163189/lhxj",
                "龙华日韩$https://cdn8.163189.xyz/163189/lhrh",
                "龙华日韩备用$http://cdn8.163189.xyz/163189/lhrh"
            ]
            
            vod_info = {
                "vod_id": "hk_live",
                "vod_name": "港澳电视直播",
                "vod_pic": "https://d.kstore.dev/download/13922/my/1770183848454_edit_80429983213246.png",
                "vod_remarks": "40个港澳电视频道",
                "vod_content": "包含TVB、亚洲卫视、有线、无线、Now、VIUTV、RTHK、Astro、澳门电视台、龙华系列等港澳电视台",
                "vod_play_from": "港澳频道",
                "vod_play_url": "#".join(hk_channels)
            }
            
            return {'list': [vod_info]}
        
        # 直播合体详情 - 读取M3U文件并按group-title分组，保留所有地址并添加序号
        elif vod_id == "hk_main":
            m3u_url = "https://raw.githubusercontent.com/Jsnzkpg/Jsnzkpg/Jsnzkpg/Jsnzkpg1.m3u"
            
            # 使用字典来存储分组，格式: { "分组名1": ["频道1-1$链接1", "频道1-2$链接2", ...], "分组名2": [...] }
            groups = {}
            # 用于存储所有频道的平铺列表，作为备用
            all_channels_fallback = []
            
            try:
                resp = requests.get(m3u_url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
                if resp.status_code == 200:
                    lines = resp.text.splitlines()
                    
                    # 用于统计每个分组内相同频道名的出现次数
                    group_channel_counters = {}
                    
                    # 逐行解析
                    for i in range(len(lines)):
                        line = lines[i].strip()
                        
                        # 找到EXTINF行
                        if line.startswith('#EXTINF:'):
                            # 提取频道名
                            channel_name = line.split(',')[-1].strip()
                            
                            # 提取分组信息
                            group_match = re.search(r'group-title="([^"]+)"', line)
                            current_group = group_match.group(1) if group_match else "未分组"
                            
                            # 初始化分组计数器
                            if current_group not in group_channel_counters:
                                group_channel_counters[current_group] = {}
                            
                            # 查找下一个有效的URL行
                            for j in range(i+1, min(i+5, len(lines))):
                                next_line = lines[j].strip()
                                if next_line.startswith('http') and not next_line.endswith('.mp4'):
                                    # 为相同频道名添加序号
                                    if channel_name in group_channel_counters[current_group]:
                                        group_channel_counters[current_group][channel_name] += 1
                                    else:
                                        group_channel_counters[current_group][channel_name] = 1
                                    
                                    # 生成带序号的频道名
                                    seq_num = group_channel_counters[current_group][channel_name]
                                    display_name = f"{channel_name}-{seq_num}"
                                    
                                    # 格式化为 "频道名-序号$播放链接"
                                    channel_entry = f"{display_name}${next_line}"
                                    
                                    # 加入分组
                                    if current_group not in groups:
                                        groups[current_group] = []
                                    groups[current_group].append(channel_entry)
                                    
                                    # 加入备用列表
                                    all_channels_fallback.append(channel_entry)
                                    break
                
                # 处理解析结果
                if groups:
                    # 有分组信息，构建多线路播放源
                    
                    # 获取所有分组名称
                    group_names = list(groups.keys())
                    
                    # 线路名称列表（每个分组单独作为一个线路）
                    play_from = "$$$".join(group_names)
                    
                    # 线路对应的播放URL列表（每个分组内的频道用#连接）
                    play_urls = []
                    for group_name in group_names:
                        channel_list = groups[group_name]
                        if channel_list:  # 只添加有频道的分组
                            play_urls.append("#".join(channel_list))
                    
                    # 最终的播放URL串，用"$$$"分隔不同线路
                    vod_play_url = "$$$".join(play_urls)
                    
                    # 计算总频道数（所有分组频道数之和）
                    total_channels = sum(len(channels) for channels in groups.values())
                    
                    vod_info = {
                        "vod_id": "hk_main",
                        "vod_name": "直播合体",
                        "vod_pic": "https://d.kstore.dev/download/13922/my/Screenshot_20260214_074021_com.larus.nova_edit_11339134734206.jpg",
                        "vod_remarks": f"从网络M3U获取，共{total_channels}个频道，{len(groups)}个分组",
                        "vod_content": "频道来源：GitHub Jsnzkpg1.m3u 文件（相同频道名已添加-1、-2序号）",
                        "vod_play_from": play_from,  # 多线路名称，用$$$分隔
                        "vod_play_url": vod_play_url   # 多线路URL，用$$$分隔
                    }
                elif all_channels_fallback:
                    # 没有分组信息但有频道，按单线路处理
                    vod_info = {
                        "vod_id": "hk_main",
                        "vod_name": "直播合体",
                        "vod_pic": "https://d.kstore.dev/download/13922/my/Screenshot_20260214_074021_com.larus.nova_edit_11339134734206.jpg",
                        "vod_remarks": f"从网络M3U获取，共{len(all_channels_fallback)}个频道（无分组）",
                        "vod_content": "频道来源：GitHub Jsnzkpg1.m3u 文件",
                        "vod_play_from": "直播合体",
                        "vod_play_url": "#".join(all_channels_fallback)
                    }
                else:
                    # 没解析到任何频道
                    vod_info = {
                        "vod_id": "hk_main",
                        "vod_name": "直播合体",
                        "vod_pic": "https://d.kstore.dev/download/13922/my/Screenshot_20260214_074021_com.larus.nova_edit_11339134734206.jpg",
                        "vod_remarks": "加载失败或无频道",
                        "vod_content": "无法从M3U文件获取频道列表",
                        "vod_play_from": "直播合体",
                        "vod_play_url": "提示$https://example.com/placeholder.m3u8"
                    }
                    
            except Exception as e:
                # 出错时记录一个错误频道
                vod_info = {
                    "vod_id": "hk_main",
                    "vod_name": "直播合体",
                    "vod_pic": "https://d.kstore.dev/download/13922/my/Screenshot_20260214_074021_com.larus.nova_edit_11339134734206.jpg",
                    "vod_remarks": f"加载失败: {str(e)[:20]}...",
                    "vod_content": "请检查网络或M3U链接是否有效",
                    "vod_play_from": "直播合体",
                    "vod_play_url": "加载失败$https://example.com/error.m3u8"
                }
            
            return {'list': [vod_info]}
        
        # ZBDS详情 - 读取TXT文件并按分组整理，保留所有地址并添加序号
        elif vod_id == "zbds":
            txt_url = "https://live.zbds.org/tv/iptv4.txt"
            
            # 使用字典来存储分组，格式: { "分组名1": ["频道1-1$链接1", "频道1-2$链接2", ...], "分组名2": [...] }
            groups = {}
            # 用于存储所有频道的平铺列表，作为备用
            all_channels_fallback = []
            
            try:
                resp = requests.get(txt_url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
                if resp.status_code == 200:
                    lines = resp.text.splitlines()
                    current_group = None  # 当前分组名
                    
                    # 用于统计每个分组内相同频道名的出现次数
                    group_channel_counters = {}
                    
                    for line in lines:
                        line = line.strip()
                        if not line:  # 跳过空行
                            continue
                        
                        # 检测分组标识行，格式如 "央视频道,#genre#"
                        if line.endswith(',#genre#'):
                            # 提取分组名，例如从 "央视频道,#genre#" 提取 "央视频道"
                            group_name = line.split(',')[0].strip()
                            if group_name:
                                current_group = group_name
                                # 确保分组在字典中存在
                                if current_group not in groups:
                                    groups[current_group] = []
                                # 初始化分组计数器
                                if current_group not in group_channel_counters:
                                    group_channel_counters[current_group] = {}
                            continue  # 继续下一行
                        
                        # 处理频道行，格式应为 "频道名,http://..."
                        if ',' in line and line.startswith('http') is False:
                            parts = line.split(',', 1)  # 只分割第一个逗号
                            if len(parts) == 2:
                                channel_name = parts[0].strip()
                                channel_url = parts[1].strip()
                                
                                # 简单的URL验证，确保是http开头且不是mp4结尾
                                if channel_url.startswith('http') and not channel_url.endswith('.mp4'):
                                    # 确定当前分组（如果没有分组，使用"默认分组"）
                                    target_group = current_group if current_group else "默认分组"
                                    
                                    # 确保分组存在
                                    if target_group not in groups:
                                        groups[target_group] = []
                                    if target_group not in group_channel_counters:
                                        group_channel_counters[target_group] = {}
                                    
                                    # 为相同频道名添加序号
                                    if channel_name in group_channel_counters[target_group]:
                                        group_channel_counters[target_group][channel_name] += 1
                                    else:
                                        group_channel_counters[target_group][channel_name] = 1
                                    
                                    # 生成带序号的频道名
                                    seq_num = group_channel_counters[target_group][channel_name]
                                    display_name = f"{channel_name}-{seq_num}"
                                    
                                    # 格式化为 "频道名-序号$播放链接"
                                    channel_entry = f"{display_name}${channel_url}"
                                    
                                    # 加入分组
                                    groups[target_group].append(channel_entry)
                                    
                                    # 同时也加入备用列表
                                    all_channels_fallback.append(channel_entry)
                
                # 处理解析结果
                if groups:
                    # 有分组信息，构建多线路播放源
                    
                    # 获取所有分组名称
                    group_names = list(groups.keys())
                    
                    # 线路名称列表（每个分组单独作为一个线路）
                    play_from = "$$$".join(group_names)
                    
                    # 线路对应的播放URL列表（每个分组内的频道用#连接）
                    play_urls = []
                    for group_name in group_names:
                        channel_list = groups[group_name]
                        if channel_list:  # 只添加有频道的分组
                            play_urls.append("#".join(channel_list))
                    
                    # 最终的播放URL串，用"$$$"分隔不同线路
                    vod_play_url = "$$$".join(play_urls)
                    
                    # 计算总频道数（所有分组频道数之和）
                    total_channels = sum(len(channels) for channels in groups.values())
                    
                    vod_info = {
                        "vod_id": "zbds",
                        "vod_name": "ZBDS",
                        "vod_pic": "https://d.kstore.dev/download/13922/my/1771027192080_edit_12441842540288.png",
                        "vod_remarks": f"从ZBDS TXT获取，共{total_channels}个频道，{len(groups)}个分组",
                        "vod_content": "频道来源：ZBDS TXT列表（相同频道名已添加-1、-2序号）",
                        "vod_play_from": play_from,  # 多线路名称，用$$$分隔
                        "vod_play_url": vod_play_url   # 多线路URL，用$$$分隔
                    }
                elif all_channels_fallback:
                    # 没有分组信息但有频道，按单线路处理
                    vod_info = {
                        "vod_id": "zbds",
                        "vod_name": "ZBDS",
                        "vod_pic": "https://d.kstore.dev/download/13922/my/1771027192080_edit_12441842540288.png",
                        "vod_remarks": f"从ZBDS TXT获取，共{len(all_channels_fallback)}个频道（无分组）",
                        "vod_content": "频道来源：ZBDS TXT列表",
                        "vod_play_from": "ZBDS",
                        "vod_play_url": "#".join(all_channels_fallback)
                    }
                else:
                    # 没解析到任何频道
                    vod_info = {
                        "vod_id": "zbds",
                        "vod_name": "ZBDS",
                        "vod_pic": "https://d.kstore.dev/download/13922/my/1771027192080_edit_12441842540288.png",
                        "vod_remarks": "加载失败或无频道",
                        "vod_content": "无法从ZBDS TXT文件获取频道列表",
                        "vod_play_from": "ZBDS",
                        "vod_play_url": "提示$https://example.com/placeholder.m3u8"
                    }
                    
            except Exception as e:
                # 出错时记录一个错误频道
                vod_info = {
                    "vod_id": "zbds",
                    "vod_name": "ZBDS",
                    "vod_pic": "https://d.kstore.dev/download/13922/my/1771027192080_edit_12441842540288.png",
                    "vod_remarks": f"加载失败: {str(e)[:20]}...",
                    "vod_content": "请检查网络或ZBDS TXT链接是否有效",
                    "vod_play_from": "ZBDS",
                    "vod_play_url": "加载失败$https://example.com/error.m3u8"
                }
            
            return {'list': [vod_info]}
        
        # TV1288详情 - 读取M3U文件并按分组整理，保留所有地址并添加序号
        elif vod_id == "tv1288":
            m3u_url = "https://ds65.tv1288.xyz"
            
            # 使用字典来存储分组，格式: { "分组名1": ["频道1-1$链接1", "频道1-2$链接2", ...], "分组名2": [...] }
            groups = {}
            # 用于存储所有频道的平铺列表，作为备用
            all_channels_fallback = []
            
            try:
                resp = requests.get(m3u_url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
                if resp.status_code == 200:
                    lines = resp.text.splitlines()
                    
                    # 用于统计每个分组内相同频道名的出现次数
                    group_channel_counters = {}
                    
                    # 逐行解析
                    for i in range(len(lines)):
                        line = lines[i].strip()
                        
                        # 找到EXTINF行
                        if line.startswith('#EXTINF:'):
                            # 提取频道名
                            channel_name = line.split(',')[-1].strip()
                            
                            # 提取分组信息
                            group_match = re.search(r'group-title="([^"]+)"', line)
                            current_group = group_match.group(1) if group_match else "未分组"
                            
                            # 初始化分组计数器
                            if current_group not in group_channel_counters:
                                group_channel_counters[current_group] = {}
                            
                            # 查找下一个有效的URL行
                            for j in range(i+1, min(i+5, len(lines))):
                                next_line = lines[j].strip()
                                if next_line.startswith('http'):  # 允许所有http开头的链接，包括带参数的
                                    # 为相同频道名添加序号
                                    if channel_name in group_channel_counters[current_group]:
                                        group_channel_counters[current_group][channel_name] += 1
                                    else:
                                        group_channel_counters[current_group][channel_name] = 1
                                    
                                    # 生成带序号的频道名
                                    seq_num = group_channel_counters[current_group][channel_name]
                                    display_name = f"{channel_name}-{seq_num}"
                                    
                                    # 格式化为 "频道名-序号$播放链接"
                                    channel_entry = f"{display_name}${next_line}"
                                    
                                    # 加入分组
                                    if current_group not in groups:
                                        groups[current_group] = []
                                    groups[current_group].append(channel_entry)
                                    
                                    # 加入备用列表
                                    all_channels_fallback.append(channel_entry)
                                    break
                
                # 处理解析结果
                if groups:
                    # 有分组信息，构建多线路播放源
                    
                    # 获取所有分组名称
                    group_names = list(groups.keys())
                    
                    # 线路名称列表（每个分组单独作为一个线路）
                    play_from = "$$$".join(group_names)
                    
                    # 线路对应的播放URL列表（每个分组内的频道用#连接）
                    play_urls = []
                    for group_name in group_names:
                        channel_list = groups[group_name]
                        if channel_list:  # 只添加有频道的分组
                            play_urls.append("#".join(channel_list))
                    
                    # 最终的播放URL串，用"$$$"分隔不同线路
                    vod_play_url = "$$$".join(play_urls)
                    
                    # 计算总频道数（所有分组频道数之和）
                    total_channels = sum(len(channels) for channels in groups.values())
                    
                    vod_info = {
                        "vod_id": "tv1288",
                        "vod_name": "TV1288",
                        "vod_pic": "https://d.kstore.dev/download/13922/my/1773896168399_edit_23497488165164.png",
                        "vod_remarks": f"从TV1288 M3U获取，共{total_channels}个频道，{len(groups)}个分组",
                        "vod_content": "频道来源：TV1288 M3U列表（相同频道名已添加-1、-2序号）",
                        "vod_play_from": play_from,  # 多线路名称，用$$$分隔
                        "vod_play_url": vod_play_url   # 多线路URL，用$$$分隔
                    }
                elif all_channels_fallback:
                    # 没有分组信息但有频道，按单线路处理
                    vod_info = {
                        "vod_id": "tv1288",
                        "vod_name": "TV1288",
                        "vod_pic": "https://d.kstore.dev/download/13922/my/1773896168399_edit_23497488165164.png",
                        "vod_remarks": f"从TV1288 M3U获取，共{len(all_channels_fallback)}个频道（无分组）",
                        "vod_content": "频道来源：TV1288 M3U列表",
                        "vod_play_from": "TV1288",
                        "vod_play_url": "#".join(all_channels_fallback)
                    }
                else:
                    # 没解析到任何频道
                    vod_info = {
                        "vod_id": "tv1288",
                        "vod_name": "TV1288",
                        "vod_pic": "https://d.kstore.dev/download/13922/my/1773896168399_edit_23497488165164.png",
                        "vod_remarks": "加载失败或无频道",
                        "vod_content": "无法从TV1288 M3U文件获取频道列表",
                        "vod_play_from": "TV1288",
                        "vod_play_url": "提示$https://example.com/placeholder.m3u8"
                    }
                    
            except Exception as e:
                # 出错时记录一个错误频道
                vod_info = {
                    "vod_id": "tv1288",
                    "vod_name": "TV1288",
                    "vod_pic": "https://d.kstore.dev/download/13922/my/1773896168399_edit_23497488165164.png",
                    "vod_remarks": f"加载失败: {str(e)[:20]}...",
                    "vod_content": "请检查网络或TV1288 M3U链接是否有效",
                    "vod_play_from": "TV1288",
                    "vod_play_url": "加载失败$https://example.com/error.m3u8"
                }
            
            return {'list': [vod_info]}
        
        return {'list': []}

    def playerContent(self, flag, id, vipFlags):
        # 提取播放链接 - 统一使用$分隔符
        if '$' in id:
            parts = id.split('$', 1)
            url = parts[1] if len(parts) > 1 else id
        else:
            url = id
        
        # 使用直播流专用UA
        headers = {
            'User-Agent': 'okhttp/4.12.0'
        }
        
        # 检查链接类型
        video_pattern = re.compile(r'https?:\/\/.*\.(?:m3u8|mp4|flv)')
        
        # 如果是直接视频链接
        if video_pattern.match(url):
            return {
                "parse": 0,
                "playUrl": '',
                "url": url,
                "header": headers
            }
        
        # 尝试获取重定向后的链接
        try:
            # 使用HEAD方法，避免下载大文件
            response = requests.head(url, headers=headers, timeout=5, 
                                   allow_redirects=True, verify=False)
            final_url = response.url
            
            # 检查Content-Type
            content_type = response.headers.get('Content-Type', '').lower()
            
            # 判断是否为直播流
            is_live_stream = (
                video_pattern.match(final_url) or
                '.m3u8' in final_url or
                'application/vnd.apple.mpegurl' in content_type or
                'audio/x-mpegurl' in content_type or
                'video/' in content_type
            )
            
            if is_live_stream:
                # 直播流，直接播放
                return {
                    "parse": 0,
                    "playUrl": '',
                    "url": final_url,
                    "header": headers
                }
            else:
                # 可能是其他类型的直播源
                return {
                    "parse": 0,
                    "playUrl": '',
                    "url": url,  # 返回原始URL
                    "header": headers
                }
                
        except Exception:
            # 请求失败，直接返回原始链接
            return {
                "parse": 0,
                "playUrl": '',
                "url": url,
                "header": headers
            }

    def searchContent(self, key, quick, pg="1"):
        # 不需要搜索功能
        return {'list': []}

    def localProxy(self, param):
        pass

    def destroy(self):
        pass