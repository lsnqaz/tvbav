 {
    "请求头": "User-Agent$Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36||Referer$https://wap.ttksgs.com/||Accept$*/*||Accept-Language$zh-CN,zh;q=0.9||Accept-Encoding$identity||Connection$keep-alive||Origin$https://wap.ttksgs.com",
    "编码": "UTF-8",
    "分类url": "https://wap.ttksgs.com/list/{cateId}.html",
    "详情url": "https://wap.ttksgs.com/vod/{vid}.html",
    "播放url": "https://wap.ttksgs.com/bo/{vid}-{play}-{page}.html",
    "分类": "电影$1#电视剧$2#综艺$3#动漫$4#动作片$6#喜剧片$7#爱情片$8#科幻片$9#恐怖片$10#剧情片$11#战争片$12#国产剧$13#香港剧$14#韩国剧$15#欧美剧$16#台湾剧$20#日本剧$21#其它剧$22#动画片$24#纪录片$23#大陆综艺$25#日韩综艺$26#港台综艺$27#欧美综艺$28#国产动漫$29#日韩动漫$30#欧美动漫$31#其它动漫$32#短剧$34#热播榜$hot",
    "主页": "https://wap.ttksgs.com/",
    "搜索url": "https://wap.ttksgs.com/search/-------------.html?wd={wd}",
    
    // 防封设置
    "安全设置": {
      "随机延迟": "2000-5000",
      "请求间隔": "3000", 
      "最大重试": 3,
      "超时时间": 15000,
      "并发控制": 2
    },
    
    // 播放解析设置
    "解析设置": {
      "预处理": "去除广告代码||执行JS",
      "提取方式": "自动嗅探视频链接", 
      "格式优先": "m3u8>mp4>flv",
      "质量排序": "4K>超清>高清>标清",
      "嗅探关键词": ".m3u8,.mp4,video,source,iframe",
      "播放器": "系统播放器||IJK播放器||EXO播放器"
    },
    
    // 浏览器模拟
    "浏览器指纹": {
      "屏幕分辨率": "1920x1080#1366x768", 
      "时区": "Asia/Shanghai",
      "语言": "zh-CN,zh;q=0.9",
      "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
    },
    
    // 解析规则
    "解析规则": {
      "首页": {
        "推荐列表": ".shoutu-vodlist .cover-img",
        "标题": ".title a@title", 
        "链接": ".title a@href",
        "图片": "@data-original",
        "描述": ".text@text",
        "状态": ".pic-text@text"
      },
      "分类页": {
        "列表": ".shoutu-vodlist .cover-img",
        "标题": ".title a@title",
        "链接": ".title a@href", 
        "图片": "@data-original",
        "描述": ".text@text",
        "状态": ".pic-text@text"
      },
      "搜索页": {
        "列表": ".shoutu-vodlist .cover-img",
        "标题": ".title a@title",
        "链接": ".title a@href",
        "图片": "@data-original", 
        "描述": ".text@text"
      },
      "详情页": {
        "标题": "h1@text",
        "导演": "p:contains(导演) a@text",
        "演员": "p:contains(主演)@html",
        "类型": ".tag a@text", 
        "地区": ".tag a@text",
        "年份": ".tag a@text",
        "简介": ".desc@text",
        "封面": ".cover-img img@data-original",
        "播放源": {
          "线路列表": ".panel:has(.panel-hd:contains(云))",
          "线路名称": ".panel-hd h3@text", 
          "剧集列表": ".shoutu-playlist li a",
          "剧集名称": "@text",
          "剧集链接": "@href"
        }
      }
    },
    
    // 线路配置
    "线路配置": {
      "自动获取": true,
      "源选择器": ".panel:has(.panel-hd:contains(云))",
      "源名称选择器": ".panel-hd h3@text", 
      "播放列表选择器": ".shoutu-playlist li a",
      "播放名称选择器": "@text",
      "播放链接选择器": "@href",
      "线路映射": {
        "腾讯云": "腾讯云",
        "字节云": "字节云", 
        "极速云": "极速云"
      }
    },
    
    // 播放源处理
    "播放源处理": {
      "合并相同剧集": true,
      "自动排序剧集": true,
      "过滤无效链接": true,
      "去重剧集名称": true
    },
    
    // 分类映射
    "分类映射": {
      "电影": "1",
      "电视剧": "2",
      "综艺": "3", 
      "动漫": "4",
      "动作片": "6",
      "喜剧片": "7",
      "爱情片": "8",
      "科幻片": "9",
      "恐怖片": "10",
      "剧情片": "11",
      "战争片": "12",
      "国产剧": "13",
      "香港剧": "14", 
      "韩国剧": "15",
      "欧美剧": "16",
      "台湾剧": "20",
      "日本剧": "21",
      "其它剧": "22",
      "动画片": "24",
      "纪录片": "23",
      "大陆综艺": "25",
      "日韩综艺": "26",
      "港台综艺": "27", 
      "欧美综艺": "28",
      "国产动漫": "29",
      "日韩动漫": "30",
      "欧美动漫": "31",
      "其它动漫": "32",
      "短剧": "34"
    },
    
    // 播放参数
    "播放参数": {
      "vid": "{vid}",
      "play": "{play}", 
      "page": "{page}"
    },
    
    // 其他设置
    "其他设置": {
      "图片代理": true,
      "强制解码": false,
      "缓存时间": 3600,
      "超时重试": true,
      "自动跳转": true,
      "线路优先": "腾讯云,字节云,极速云"
    }
  }