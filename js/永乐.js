{
"请求头": "User-Agent$Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36||Referer$https://www.ylsp.lv/||Accept$*/*||Accept-Language$zh-CN,zh;q=0.9||Accept-Encoding$identity||Connection$keep-alive||Origin$https://www.ylsp.lv/",
"编码": "UTF-8",
"分类url": "https://www.ylsp.lv/vodtype/{cateId}/",
"详情url": "https://www.ylsp.lv/voddetail/{vid}/",
"播放url": "https://www.ylsp.lv/vodplay/{vid}-{play}-{page}.html",
"分类": "电影$1#剧集$2#综艺$3#动漫$4",
"主页": "https://www.ylsp.lv/",
"搜索url": "https://www.ylsp.lv/vodsearch/{wd}/",
// 防封设置
"安全设置": {
  "随机延迟": "2000-5000",
  "请求间隔": "3000",
  "最大重试": "3",
  "超时时间": "15000",
  "并发控制": "2"
},

// 播放解析设置
"解析设置": {
  "预处理": "去除广告代码||执行JS",
  "提取方式": "自动嗅探视频链接",
  "格式优先": "m3u8>mp4>flv",
  "质量排序": "4K>超清>高清>标清",
  "嗅探关键词": ".m3u8,.mp4,video,source,iframe"
},

// 浏览器模拟
"浏览器指纹": {
  "屏幕分辨率": "1920x1080#1366x768",
  "时区": "Asia/Shanghai",
  "语言": "zh-CN,zh;q=0.9"
}
}