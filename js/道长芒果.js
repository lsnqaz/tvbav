var rule = {
    title:'百忙无果[官]',
    host:'https://pianku.api.%6d%67%74%76.com',
    homeUrl:'',
    // 更新为v2接口，使用手机端接口绕过验证
    searchUrl:'https://mobileso.bz.%6d%67%74%76.com/msite/search/v2?q=**&pn=fypage&pc=10',
    detailUrl:'https://pcweb.api.mgtv.com/episode/list?page=1&size=50&video_id=fyid',
    searchable:2,
    quickSearch:1, // 启用快速搜索
    filterable:1,
    multi:1,
    // 分类链接fypage参数支持1个()表达式
    // https://www.mgtv.com/lib/3?lastp=list_index&kind=a1&year=all&chargeInfo=a1&sort=c2
    url:'/rider/list/pcweb/v3?platform=pcweb&channelId=fyclass&pn=fypage&pc=80&hudong=1&_support=10000000&kind=a1&area=a1',
    filter_url:'year={{fl.year or "all"}}&sort={{fl.sort or "all"}}&chargeInfo={{fl.chargeInfo or "all"}}',
    headers:{
        'User-Agent':'PC_UA'
    },
    timeout:5000,
    class_name:'电视剧&电影&综艺&动漫&纪录片&教育&少儿',
    class_url:'2&3&1&50&51&115&10',
    filter:{
        "1": [{
            "key": "chargeInfo",
            "name": "付费类型",
            "value": [{
                "n": "全部",
                "v": "all"
            }, {
                "n": "免费",
                "v": "b1"
            }, {
                "n": "vip",
                "v": "b2"
            }, {
                "n": "VIP用券",
                "v": "b3"
            }, {
                "n": "付费点播",
                "v": "b4"
            }]
        }, {
            "key": "sort",
            "name": "排序",
            "value": [{
                "n": "最新",
                "v": "c1"
            }, {
                "n": "最热",
                "v": "c2"
            }, {
                "n": "知乎高分",
                "v": "c4"
            }]
        }, {
            "key": "year",
            "name": "年代",
            "value": [{
                "n": "全部",
                "v": "all"
            }, {
                "n": "2025",
                "v": "2025"
            }, {
                "n": "2024",
                "v": "2024"
            }, {
                "n": "2023",
                "v": "2023"
            }, {
                "n": "2022",
                "v": "2022"
            }, {
                "n": "2021",
                "v": "2021"
            }, {
                "n": "2020",
                "v": "2020"
            }, {
                "n": "2019",
                "v": "2019"
            }, {
                "n": "2018",
                "v": "2018"
            }, {
                "n": "2017",
                "v": "2017"
            }, {
                "n": "2016",
                "v": "2016"
            }, {
                "n": "2015",
                "v": "2015"
            }, {
                "n": "2014",
                "v": "2014"
            }, {
                "n": "2013",
                "v": "2013"
            }, {
                "n": "2012",
                "v": "2012"
            }, {
                "n": "2011",
                "v": "2011"
            }, {
                "n": "2010",
                "v": "2010"
            }, {
                "n": "2009",
                "v": "2009"
            }, {
                "n": "2008",
                "v": "2008"
            }, {
                "n": "2007",
                "v": "2007"
            }, {
                "n": "2006",
                "v": "2006"
            }, {
                "n": "2005",
                "v": "2005"
            }, {
                "n": "2004",
                "v": "2004"
            }]
        }],
        "2": [{
            "key": "chargeInfo",
            "name": "付费类型",
            "value": [{
                "n": "全部",
                "v": "all"
            }, {
                "n": "免费",
                "v": "b1"
            }, {
                "n": "vip",
                "v": "b2"
            }, {
                "n": "VIP用券",
                "v": "b3"
            }, {
                "n": "付费点播",
                "v": "b4"
            }]
        }, {
            "key": "sort",
            "name": "排序",
            "value": [{
                "n": "最新",
                "v": "c1"
            }, {
                "n": "最热",
                "v": "c2"
            }, {
                "n": "知乎高分",
                "v": "c4"
            }]
        }, {
            "key": "year",
            "name": "年代",
            "value": [{
                "n": "全部",
                "v": "all"
            }, {
                "n": "2025",
                "v": "2025"
            }, {
                "n": "2024",
                "v": "2024"
            }, {
                "n": "2023",
                "v": "2023"
            }, {
                "n": "2022",
                "v": "2022"
            }, {
                "n": "2021",
                "v": "2021"
            }, {
                "n": "2020",
                "v": "2020"
            }, {
                "n": "2019",
                "v": "2019"
            }, {
                "n": "2018",
                "v": "2018"
            }, {
                "n": "2017",
                "v": "2017"
            }, {
                "n": "2016",
                "v": "2016"
            }, {
                "n": "2015",
                "v": "2015"
            }, {
                "n": "2014",
                "v": "2014"
            }, {
                "n": "2013",
                "v": "2013"
            }, {
                "n": "2012",
                "v": "2012"
            }, {
                "n": "2011",
                "v": "2011"
            }, {
                "n": "2010",
                "v": "2010"
            }, {
                "n": "2009",
                "v": "2009"
            }, {
                "n": "2008",
                "v": "2008"
            }, {
                "n": "2007",
                "v": "2007"
            }, {
                "n": "2006",
                "v": "2006"
            }, {
                "n": "2005",
                "v": "2005"
            }, {
                "n": "2004",
                "v": "2004"
            }]
        }],
        "3": [{
            "key": "chargeInfo",
            "name": "付费类型",
            "value": [{
                "n": "全部",
                "v": "all"
            }, {
                "n": "免费",
                "v": "b1"
            }, {
                "n": "vip",
                "v": "b2"
            }, {
                "n": "VIP用券",
                "v": "b3"
            }, {
                "n": "付费点播",
                "v": "b4"
            }]
        }, {
            "key": "sort",
            "name": "排序",
            "value": [{
                "n": "最新",
                "v": "c1"
            }, {
                "n": "最热",
                "v": "c2"
            }, {
                "n": "知乎高分",
                "v": "c4"
            }]
        }, {
            "key": "year",
            "name": "年代",
            "value": [{
                "n": "全部",
                "v": "all"
            }, {
                "n": "2025",
                "v": "2025"
            }, {
                "n": "2024",
                "v": "2024"
            }, {
                "n": "2023",
                "v": "2023"
            }, {
                "n": "2022",
                "v": "2022"
            }, {
                "n": "2021",
                "v": "2021"
            }, {
                "n": "2020",
                "v": "2020"
            }, {
                "n": "2019",
                "v": "2019"
            }, {
                "n": "2018",
                "v": "2018"
            }, {
                "n": "2017",
                "v": "2017"
            }, {
                "n": "2016",
                "v": "2016"
            }, {
                "n": "2015",
                "v": "2015"
            }, {
                "n": "2014",
                "v": "2014"
            }, {
                "n": "2013",
                "v": "2013"
            }, {
                "n": "2012",
                "v": "2012"
            }, {
                "n": "2011",
                "v": "2011"
            }, {
                "n": "2010",
                "v": "2010"
            }, {
                "n": "2009",
                "v": "2009"
            }, {
                "n": "2008",
                "v": "2008"
            }, {
                "n": "2007",
                "v": "2007"
            }, {
                "n": "2006",
                "v": "2006"
            }, {
                "n": "2005",
                "v": "2005"
            }, {
                "n": "2004",
                "v": "2004"
            }]
        }],
        "50": [{
            "key": "chargeInfo",
            "name": "付费类型",
            "value": [{
                "n": "全部",
                "v": "all"
            }, {
                "n": "免费",
                "v": "b1"
            }, {
                "n": "vip",
                "v": "b2"
            }, {
                "n": "VIP用券",
                "v": "b3"
            }, {
                "n": "付费点播",
                "v": "b4"
            }]
        }, {
            "key": "sort",
            "name": "排序",
            "value": [{
                "n": "最新",
                "v": "c1"
            }, {
                "n": "最热",
                "v": "c2"
            }, {
                "n": "知乎高分",
                "v": "c4"
            }]
        }, {
            "key": "year",
            "name": "年代",
            "value": [{
                "n": "全部",
                "v": "all"
            }, {
                "n": "2025",
                "v": "2025"
            }, {
                "n": "2024",
                "v": "2024"
            }, {
                "n": "2023",
                "v": "2023"
            }, {
                "n": "2022",
                "v": "2022"
            }, {
                "n": "2021",
                "v": "2021"
            }, {
                "n": "2020",
                "v": "2020"
            }, {
                "n": "2019",
                "v": "2019"
            }, {
                "n": "2018",
                "v": "2018"
            }, {
                "n": "2017",
                "v": "2017"
            }, {
                "n": "2016",
                "v": "2016"
            }, {
                "n": "2015",
                "v": "2015"
            }, {
                "n": "2014",
                "v": "2014"
            }, {
                "n": "2013",
                "v": "2013"
            }, {
                "n": "2012",
                "v": "2012"
            }, {
                "n": "2011",
                "v": "2011"
            }, {
                "n": "2010",
                "v": "2010"
            }, {
                "n": "2009",
                "v": "2009"
            }, {
                "n": "2008",
                "v": "2008"
            }, {
                "n": "2007",
                "v": "2007"
            }, {
                "n": "2006",
                "v": "2006"
            }, {
                "n": "2005",
                "v": "2005"
            }, {
                "n": "2004",
                "v": "2004"
            }]
        }],
        "51": [{
            "key": "chargeInfo",
            "name": "付费类型",
            "value": [{
                "n": "全部",
                "v": "all"
            }, {
                "n": "免费",
                "v": "b1"
            }, {
                "n": "vip",
                "v": "b2"
            }, {
                "n": "VIP用券",
                "v": "b3"
            }, {
                "n": "付费点播",
                "v": "b4"
            }]
        }, {
            "key": "sort",
            "name": "排序",
            "value": [{
                "n": "最新",
                "v": "c1"
            }, {
                "n": "最热",
                "v": "c2"
            }, {
                "n": "知乎高分",
                "v": "c4"
            }]
        }, {
            "key": "year",
            "name": "年代",
            "value": [{
                "n": "全部",
                "v": "all"
            }, {
                "n": "2025",
                "v": "2025"
            }, {
                "n": "2024",
                "v": "2024"
            }, {
                "n": "2023",
                "v": "2023"
            }, {
                "n": "2022",
                "v": "2022"
            }, {
                "n": "2021",
                "v": "2021"
            }, {
                "n": "2020",
                "v": "2020"
            }, {
                "n": "2019",
                "v": "2019"
            }, {
                "n": "2018",
                "v": "2018"
            }, {
                "n": "2017",
                "v": "2017"
            }, {
                "n": "2016",
                "v": "2016"
            }, {
                "n": "2015",
                "v": "2015"
            }, {
                "n": "2014",
                "v": "2014"
            }, {
                "n": "2013",
                "v": "2013"
            }, {
                "n": "2012",
                "v": "2012"
            }, {
                "n": "2011",
                "v": "2011"
            }, {
                "n": "2010",
                "v": "2010"
            }, {
                "n": "2009",
                "v": "2009"
            }, {
                "n": "2008",
                "v": "2008"
            }, {
                "n": "2007",
                "v": "2007"
            }, {
                "n": "2006",
                "v": "2006"
            }, {
                "n": "2005",
                "v": "2005"
            }, {
                "n": "2004",
                "v": "2004"
            }]
        }],
        "115": [{
            "key": "chargeInfo",
            "name": "付费类型",
            "value": [{
                "n": "全部",
                "v": "all"
            }, {
                "n": "免费",
                "v": "b1"
            }, {
                "n": "vip",
                "v": "b2"
            }, {
                "n": "VIP用券",
                "v": "b3"
            }, {
                "n": "付费点播",
                "v": "b4"
            }]
        }, {
            "key": "sort",
            "name": "排序",
            "value": [{
                "n": "最新",
                "v": "c1"
            }, {
                "n": "最热",
                "v": "c2"
            }, {
                "n": "知乎高分",
                "v": "c4"
            }]
        }, {
            "key": "year",
            "name": "年代",
            "value": [{
                "n": "全部",
                "v": "all"
            }, {
                "n": "2025",
                "v": "2025"
            }, {
                "n": "2024",
                "v": "2024"
            }, {
                "n": "2023",
                "v": "2023"
            }, {
                "n": "2022",
                "v": "2022"
            }, {
                "n": "2021",
                "v": "2021"
            }, {
                "n": "2020",
                "v": "2020"
            }, {
                "n": "2019",
                "v": "2019"
            }, {
                "n": "2018",
                "v": "2018"
            }, {
                "n": "2017",
                "v": "2017"
            }, {
                "n": "2016",
                "v": "2016"
            }, {
                "n": "2015",
                "v": "2015"
            }, {
                "n": "2014",
                "v": "2014"
            }, {
                "n": "2013",
                "v": "2013"
            }, {
                "n": "2012",
                "v": "2012"
            }, {
                "n": "2011",
                "v": "2011"
            }, {
                "n": "2010",
                "v": "2010"
            }, {
                "n": "2009",
                "v": "2009"
            }, {
                "n": "2008",
                "v": "2008"
            }, {
                "n": "2007",
                "v": "2007"
            }, {
                "n": "2006",
                "v": "2006"
            }, {
                "n": "2005",
                "v": "2005"
            }, {
                "n": "2004",
                "v": "2004"
            }]
        }]
    },
    limit:20,
    play_parse:true,
    lazy: $js.toString(() => {
    // 1. 准备视频原始地址和需要的变量
    let api = "" + input.split("?")[0];
    let videoUrl = api; // 待解析的视频地址
    let danmaku = "http://127.0.0.1:9978/proxy?do=danmu&site=js&url=http://dm.qxq6.com/zy/api.php?url=" + videoUrl;
    console.log("原始视频地址：" + videoUrl);

    // 2. 尝试获取并优先使用tvb.json配置的parses列表
    //    注意：此变量名(RULES.parse_list)可能因APP不同而异，常见的有 PARSE、parses、parse_list
    let parseList = [];
    try {
        // 方式一：尝试读取RULES中的解析列表 (常见于TVBox、CatVod等)
        if (typeof(RULES) !== 'undefined' && RULES.parse_list && RULES.parse_list.length > 0) {
            parseList = RULES.parse_list;
            console.log("从RULES.parse_list获取到解析器列表，数量：" + parseList.length);
        }
        // 方式二：尝试读取PARSE列表 (某些版本)
        else if (typeof(PARSE) !== 'undefined' && PARSE.length > 0) {
            parseList = PARSE;
            console.log("从PARSE获取到解析器列表，数量：" + parseList.length);
        }
        // 方式三：尝试从全局配置读取
        else if (typeof(getParseList) === 'function') {
            parseList = getParseList();
            console.log("通过getParseList()获取解析器列表，数量：" + parseList.length);
        }
        else {
            // 如果无法获取列表，使用一个包含"无上"解析的简易备份列表
            console.log("未找到解析器列表，使用备用列表");
            parseList = [
                {
                    "name": "无上",
                    "url": "https://mfjx.iwsyy.xyz/?url=",
                    "type": 1,
                    "ext": { "header": { "User-Agent": "okhttp/4.9.1" } }
                },
                {
                    "name": "巧技",
                    "url": "https://zy.qiaoji8.com/neibu.php?url=",
                    "type": 1,
                    "ext": { "header": { "User-Agent": "okhttp/4.9.1" } }
                },
                {
                    "name": "极速",
                    "url": "https://jx.2s0.cn/player/?url=",
                    "type": 0
                }
            ];
        }
    } catch (e) {
        console.log("获取解析器列表时出错：" + e.message);
        // 出错时使用备用列表
        parseList = [
            {
                "name": "无上",
                "url": "https://mfjx.iwsyy.xyz/?url=",
                "type": 1,
                "ext": { "header": { "User-Agent": "okhttp/4.9.1" } }
            }
        ];
    }

    // 3. 轮询尝试每个解析器
    let finalUrl = '';
    let usedParser = '';
    let isMgtvSource = videoUrl.includes("mgtv"); // 判断是否为芒果源

    for (let i = 0; i < parseList.length; i++) {
        let parser = parseList[i];
        let parseUrl = parser.url + encodeURIComponent(videoUrl);
        console.log(`尝试解析器[${i+1}/${parseList.length}]：${parser.name}，地址：${parseUrl}`);

        try {
            // 发送请求测试解析器
            let response = fetch(parseUrl, {
                method: 'get',
                headers: {
                    'User-Agent': parser.ext && parser.ext.header ? parser.ext.header['User-Agent'] : 'okhttp/3.14.9',
                    'Referer': 'https://www.mgtv.com',
                    ...(parser.ext && parser.ext.header ? parser.ext.header : {})
                },
                timeout: 8000 // 8秒超时
            });

            // 检查响应是否有效（这里简化处理，实际可能需要根据返回内容判断）
            if (response && response.status === 200) {
                // 对于type 1解析器（返回JSON），尝试解析
                if (parser.type === 1) {
                    let result = JSON.parse(response);
                    if (result && result.url) {
                        finalUrl = result.url;
                        usedParser = parser.name;
                        console.log(`✅ 解析器 ${parser.name} 成功，获得播放地址`);
                        break; // 成功，跳出循环
                    }
                } else {
                    // 对于type 0解析器（返回HTML/直接播放地址），使用解析后的地址
                    finalUrl = parseUrl;
                    usedParser = parser.name;
                    console.log(`✅ 解析器 ${parser.name} 成功，使用解析地址`);
                    break;
                }
            }
        } catch (error) {
            console.log(`❌ 解析器 ${parser.name} 失败：${error.message}`);
            continue; // 继续尝试下一个
        }
    }

    // 4. 根据结果设置最终的input
    if (finalUrl) {
        console.log(`🎉 最终使用解析器：${usedParser}`);
        input = {
            parse: 0, // 0表示直接播放，1表示需要二次解析
            url: finalUrl,
            jx: finalUrl.includes('jx.') || finalUrl.includes('jiexi') ? 1 : 0, // 如果是解析地址则标记jx=1
            danmaku: danmaku
        };
    } else {
        console.log("❌ 所有解析器均失败，尝试使用原始地址+默认解析");
        // 所有解析器都失败，降级到原始逻辑
        try {
            let response = fetch(videoUrl, {
                method: 'get',
                headers: {
                    'User-Agent': 'okhttp/3.14.9',
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
            });
            let bata = JSON.parse(response);
            if (bata.url && bata.url.includes("mgtv")) {
                input = {
                    parse: 0,
                    url: bata.url,
                    jx: 0,
                    danmaku: danmaku
                };
            } else {
                // 使用第一个解析器作为最后的尝试
                let lastParser = parseList[0] || { url: "https://mfjx.iwsyy.xyz/?url=" };
                input = {
                    parse: 0,
                    url: lastParser.url + encodeURIComponent(videoUrl),
                    jx: 1,
                    danmaku: danmaku
                };
            }
        } catch (e) {
            console.log("降级方案也失败，使用最保守方式");
            input = {
                parse: 0,
                url: videoUrl,
                jx: 1,
                danmaku: danmaku
            };
        }
    }
    console.log("最终input设置：" + JSON.stringify(input));
}),
    // 推荐:'.list_item;img&&alt;img&&src;a&&Text;a&&data-float',
    一级:'json:data.hitDocs;title;img;updateInfo||rightCorner.text;playPartId',
    // 一级:'json:data.hitDocs;title;img;updateInfo;playPartId',
    二级: $js.toString(() => {
        fetch_params.headers.Referer = "https://www.mgtv.com";
        fetch_params.headers["User-Agent"] = MOBILE_UA;
        pdfh = jsp.pdfh;
        pdfa = jsp.pdfa;
        pd = jsp.pd;
        VOD = {};
        let d = [];
        let html = request(input);
        let json = JSON.parse(html);
        let host = "https://www.mgtv.com";
        let ourl = json.data.list.length > 0 ? json.data.list[0].url : json.data.series[0].url;
        if (!/^http/.test(ourl)) {
            ourl = host + ourl
        }
        fetch_params.headers["User-Agent"] = MOBILE_UA;
        html = request(ourl);
        if (html.includes("window.location =")) {
            print("开始获取ourl");
            ourl = pdfh(html, "meta[http-equiv=refresh]&&content").split("url=")[1];
            print("获取到ourl:" + ourl);
            html = request(ourl)
        }
        try {
            let details = pdfh(html, ".m-details&&Html").replace(/h1>/, "h6>").replace(/div/g, "br");
            print(details);
            let actor = "",
                director = "",
                time = "";
            if (/播出时间/.test(details)) {
                actor = pdfh(html, "p:eq(5)&&Text").substr(0, 25);
                director = pdfh(html, "p:eq(4)&&Text");
                time = pdfh(html, "p:eq(3)&&Text")
            } else {
                actor = pdfh(html, "p:eq(4)&&Text").substr(0, 25);
                director = pdfh(html, "p:eq(3)&&Text");
                time = "已完结"
            }
            let _img = pd(html, ".video-img&&img&&src");
            let JJ = pdfh(html, ".desc&&Text").split("简介：")[1];
            let _desc = time;
            VOD.vod_name = pdfh(html, ".vt-txt&&Text");
            VOD.type_name = pdfh(html, "p:eq(0)&&Text").substr(0, 6);
            VOD.vod_area = pdfh(html, "p:eq(1)&&Text");
            VOD.vod_actor = actor;
            VOD.vod_director = director;
            VOD.vod_remarks = _desc;
            VOD.vod_pic = _img;
            VOD.vod_content = JJ;
            if (!VOD.vod_name) {
                VOD.vod_name = VOD.type_name;
            }
        } catch (e) {
            log("获取影片信息发生错误:" + e.message)
        }

        function getRjpg(imgUrl, xs) {
            xs = xs || 3;
            let picSize = /jpg_/.test(imgUrl) ? imgUrl.split("jpg_")[1].split(".")[0] : false;
            let rjpg = false;
            if (picSize) {
                let a = parseInt(picSize.split("x")[0]) * xs;
                let b = parseInt(picSize.split("x")[1]) * xs;
                rjpg = a + "x" + b + ".jpg"
            }
            let img = /jpg_/.test(imgUrl) && rjpg ? imgUrl.replace(imgUrl.split("jpg_")[1], rjpg) : imgUrl;
            return img
        }

        if (json.data.total === 1 && json.data.list.length === 1) {
            let data = json.data.list[0];
            let url = "https://www.mgtv.com" + data.url;
            d.push({
                title: data.t4,
                desc: data.t2,
                pic_url: getRjpg(data.img),
                url: url
            })
        } else if (json.data.list.length > 1) {
            for (let i = 1; i <= json.data.total_page; i++) {
                if (i > 1) {
                    json = JSON.parse(fetch(input.replace("page=1", "page=" + i), {}))
                }
                json.data.list.forEach(function(data) {
                    let url = "https://www.mgtv.com" + data.url;
                    if (data.isIntact == "1") {
                        d.push({
                            title: data.t4,
                            desc: data.t2,
                            pic_url: getRjpg(data.img),
                            url: url
                        })
                    }
                })
            }
        } else {
            print(input + "暂无片源")
        }
        VOD.vod_play_from = "mgtv";
        VOD.vod_play_url = d.map(function(it) {
            return it.title + "$" + it.url
        }).join("#");
        setResult(d);
    }),

    搜索: $js.toString(() => {
        fetch_params.headers.Referer = "https://www.mgtv.com";
        fetch_params.headers["User-Agent"] = MOBILE_UA;
        let d = [];
        let html = request(input);
        let json = JSON.parse(html);
        json.data.contents.forEach(function(data) {
            if (data.type && data.type == 'media') {
                let item = data.data[0];
                let desc = item.desc.join(',');
                let fyclass = '';
                if (item.source === "imgo") {
                    let img = item.img ? item.img : '';
                    try {
                        fyclass = item.rpt.match(/idx=(.*?)&/)[1] + '$';
                    } catch (e) {
                        log(e.message);
                        fyclass = '';
                    }
                    log(fyclass);
                    d.push({
                        title: item.title.replace(/<B>|<\/B>/g, ''),
                        img: img,
                        content: '',
                        desc: desc,
                        url: fyclass + item.url.match(/.*\/(.*?)\.html/)[1]
                    })
                }
            }
        });
        setResult(d);
    }),
}