{
    "请求头": "User-Agent$Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36||Referer$https://www.zjkrmv.vip/",
    "编码": "UTF-8",
    "分类url": "https://www.zjkrmv.vip/vodshow/{cateId}-----------{page}.html",
    "详情url": "https://www.zjkrmv.vip/voddetail/{vid}.html",
    "播放url": "https://www.zjkrmv.vip/vodplay/{vid}-{play}-{page}.html",
    "分类": "电影$1#电视剧$2#综艺$3#动漫$4#午夜$37#国产剧$13#港台剧$14#日韩剧$15#欧美剧$16#周番剧表$weekday#国产动漫$国产动漫",
    "主页": "https://www.zjkrmv.vip/",
    "搜索url": "https://www.zjkrmv.vip/index.php/vod/search/page/{page}/wd/{wd}.html",
    "备用域名": ["https://www.zjkrmv.com/", "https://www.zjkrmv.vip/"],
    
    // 修正后的数据解析 - 适配实际HTML结构
    "数据解析": {
        "分类列表": ".public-list-box",
        "列表项": {
            "视频ID": "a[href*='voddetail']/@href | split:/(\\d+)\\.html | get:0",
            "标题": ".time-title/@title | .time-title/text()",
            "封面": ".public-list-exp img/@data-src | .gen-movie-img/@data-src",
            "描述": ".public-list-subtitle/text()",
            "类型": ".public-prt/text()",
            "状态": ".public-list-prb/text()"
        },
        "首页推荐": {
            "轮播图": ".slid-e",
            "推荐列表": ".list-vod .public-list-box, .vod-type-module .public-list-box",
            "轮播项": {
                "视频ID": "a[href*='voddetail']/@href | split:/(\\d+)\\.html | get:0",
                "标题": ".slide-info-title/text()",
                "封面": ".slide-time-img3/@data-background",
                "描述": ".slide-info/text()",
                "类型": ".slid-e-type/text()",
                "状态": ""
            }
        },
        "每日更新": {
            "容器": "#week-module-box",
            "每日模块": "#week-module-1, #week-module-2, #week-module-3, #week-module-4, #week-module-5, #week-module-6, #week-module-7",
            "每日项": {
                "视频ID": "a[href*='voddetail']/@href | split:/(\\d+)\\.html | get:0",
                "标题": ".vod-name/text() | .vod-name/@title",
                "封面": ".vod-pic/@data-src | .vod-pic/@src",
                "描述": ".vod-subtitle/text()",
                "类型": ".vod-tag/text()",
                "状态": ".vod-remarks/text()"
            }
        }
    },
    
    // 播放源解析配置
    "播放源解析": {
        "播放列表": ".module-play-list, .his-tab-list",
        "播放项": {
            "集数名称": ".episode-item/text() | @title",
            "播放链接": "@href",
            "播放标识": "@href | regex:/vodplay/(\\d+)-(\\d+)-(\\d+)\\.html | join:-"
        },
        "线路分类": ".module-tab-items-box .module-tab-item span/text()"
    },
    
    // 详情页额外信息
    "详情页信息": {
        "导演": ".module-info-introduction-content .director/text() | regex:导演[:：]\\s*(.+?)\\s*$",
        "演员": ".module-info-introduction-content .actor/text() | regex:主演[:：]\\s*(.+?)\\s*$",
        "年份": ".module-info-introduction-content .year/text() | regex:年份[:：]\\s*(.+?)\\s*$",
        "地区": ".module-info-introduction-content .area/text() | regex:地区[:：]\\s*(.+?)\\s*$",
        "简介": ".module-info-introduction-content .content/text()"
    },
    
    "安全设置": {
        "随机延迟": "1000-3000",
        "请求间隔": "2000",
        "最大重试": "2",
        "超时时间": "10000",
        "启用缓存": "true",
        "缓存时间": "3600"
    },
    
    // 高级配置
    "高级配置": {
        "启用JS渲染": "true",
        "启用图片懒加载": "true",
        "启用Ajax加载": "true",
        "启用反爬检测": "true",
        "启用自动重试": "true",
        "重试次数": "3",
        "启用备用域名": "true"
    },
    
    // 页面元素验证
    "页面验证": {
        "首页验证元素": ".slid-e, .public-list-box",
        "分类页验证元素": ".public-list-box",
        "详情页验证元素": ".module-info-heading, .module-play-list",
        "搜索页验证元素": "#resultList, .module-card-items"
    }
}