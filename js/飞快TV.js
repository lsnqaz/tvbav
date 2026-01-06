{
    "请求头": "User-Agent$Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36||Referer$https://feikuai.tv/||Accept$*/*||Accept-Language$zh-CN,zh;q=0.9||Accept-Encoding$identity||Connection$keep-alive||Origin$https://feikuai.tv",
    "编码": "UTF-8",
    "分类url": "https://feikuai.tv/vodtype/{cateId}.html",
    "详情url": "https://feikuai.tv/voddetail/{vid}.html",
    "播放url": "https://feikuai.tv/vodplay/{vid}-{play}-{page}.html",
    "分类": "电影$1#剧集$2#综艺$3#动漫$4",
    "主页": "https://feikuai.tv/",
    "搜索url": "https://feikuai.tv/vodsearch/{wd}/",
    
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