{
    "请求头": "User-Agent$Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36||Referer$http://www.fimled.com/||Accept$*/*||Accept-Language$zh-CN,zh;q=0.9||Accept-Encoding$identity||Connection$keep-alive||Origin$http://www.fimled.com",
    "编码": "UTF-8",
    "分类url": "http://www.fimled.com/tfiu/{cateId}.html",
    "详情url": "http://www.fimled.com/dmlq/{vid}.html",
    "播放url": "http://www.fimled.com/peds/{vid}-{play}-{page}.html",
    "分类": "电影$1#电视剧$2#综艺$3#动漫$4#短剧$36#最新更新$new#热榜$hot",
    "主页": "http://www.fimled.com/",
    "搜索url": "http://www.fimled.com/search/-------------.html?wd={wd}",
    
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
    
    // 解析规则 - 修复线路显示
    "解析规则": {
      "首页": {
        "推荐列表": ".stui-vodlist__box",
        "标题": ".title a@title",
        "链接": ".title a@href",
        "图片": ".stui-vodlist__thumb@data-original",
        "描述": ".text@text",
        "状态": ".pic-text@text"
      },
      "分类页": {
        "列表": ".stui-vodlist__box",
        "标题": ".title a@title",
        "链接": ".title a@href",
        "图片": ".stui-vodlist__thumb@data-original",
        "演员": ".text@text",
        "状态": ".pic-text@text"
      },
      "搜索页": {
        "列表": ".stui-vodlist__media li",
        "标题": ".title a@text",
        "链接": ".title a@href",
        "图片": ".v-thumb@data-original",
        "导演": "p:contains(导演) a@text",
        "演员": "p:contains(主演)@html",
        "类型": "p:contains(类型) a@text"
      },
      "详情页": {
        "标题": ".title@text",
        "导演": ".data:contains(导演) a@text",
        "演员": ".data:contains(主演)@html",
        "类型": ".data:contains(类型) a@text",
        "地区": ".data:contains(地区) a@text",
        "年份": ".data:contains(年份) a@text",
        "简介": ".desc@text",
        "封面": ".stui-vodlist__thumb@data-original",
        "播放源": {
          "线路列表": ".nav-tabs li",
          "线路名称": "a@text",
          "线路标识": "a@data-toggle",
          "剧集列表": ".tab-pane .stui-content__playlist li a",
          "剧集名称": "@text",
          "剧集链接": "@href"
        }
      }
    },
    
    // 线路配置 - 修复线路名称显示
    "线路配置": {
      "自动获取": true,
      "源选择器": ".nav-tabs li a",
      "源名称选择器": "@text",
      "源标识选择器": "@data-toggle",
      "播放列表选择器": ".tab-pane .stui-content__playlist li a",
      "播放名称选择器": "@text",
      "播放链接选择器": "@href",
      "线路映射": {
        "playlist1": "小米云",
        "playlist2": "极速云",
        "playlist3": "华为云"
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
      "短剧": "36",
      "剧情片": "11",
      "动作片": "6",
      "喜剧片": "7",
      "爱情片": "8",
      "科幻片": "9",
      "恐怖片": "10",
      "国产剧": "13",
      "香港剧": "14"
    },
    
    // 播放参数
    "播放参数": {
      "vid": "{vid}",
      "play": "{play}",
      "page": "{page}",
      "from": "ffm3u8",
      "server": "no"
    },
    
    // 其他设置
    "其他设置": {
      "图片代理": true,
      "强制解码": false,
      "缓存时间": 3600,
      "超时重试": true,
      "自动跳转": true,
      "线路优先": "小米云,极速云,华为云"
    }
  }
