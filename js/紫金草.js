{
    "请求头": "User-Agent$Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36||Referer$https://www.zjcvod.com/||Accept$*/*||Accept-Language$zh-CN,zh;q=0.9||Accept-Encoding$identity||Connection$keep-alive||Origin$https://www.zjcvod.com",
    "编码": "UTF-8",
    "分类url": "https://www.zjcvod.com/vodtype/{cateId}.html",
    "详情url": "https://www.zjcvod.com/voddetail/{vid}.html",
    "播放url": "https://www.zjcvod.com/vodplay/{vid}-{play}-{page}.html",
    "分类": "连续剧$lianxuju#电影$dianying#综艺$zongyi#动漫$dongman#短剧$duanju#少儿$shaoer#Netflix$Netflix#纪录片$jilupian",
    "主页": "https://www.zjcvod.com/",
    "搜索url": "https://www.zjcvod.com/vodsearch/{wd}/",
    
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
      "嗅探关键词": ".m3u8,.mp4,video,source,iframe",
      "图片代理": "https://www.zjcvod.com/img.php?url={img}"
    },
    
    // 浏览器模拟
    "浏览器指纹": {
      "屏幕分辨率": "1920x1080#1366x768",
      "时区": "Asia/Shanghai",
      "语言": "zh-CN,zh;q=0.9"
    },
    
    // 特殊处理
    "特殊设置": {
      "图片懒加载": "lazyload",
      "数据源": "data-original",
      "搜索方法": "POST"
    }
  }