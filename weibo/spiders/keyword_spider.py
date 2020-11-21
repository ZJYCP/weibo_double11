import scrapy
# from scrapy import log
import js2xml
from weibo.items import WeiboItem
import urllib.parse as parse

class KeywordSpider(scrapy.Spider):
    name = "keyword"
    allowed_domains = ['s.weibo.com','m.weibo.cn']

    # start_urls = [
    #     'https://s.weibo.com/weibo?q=%E5%8F%8C%E5%8D%81%E4%B8%80&scope=ori&suball=1&timescope=custom:2020-11-15-0:2020-11-15-1&Refer=g&page=1',
    #     'https://s.weibo.com/weibo?q=%E5%8F%8C%E5%8D%81%E4%B8%80&scope=ori&suball=1&timescope=custom:2020-11-15-1:2020-11-15-2&Refer=g&page=1',
    #     'https://s.weibo.com/weibo?q=%E5%8F%8C%E5%8D%81%E4%B8%80&scope=ori&suball=1&timescope=custom:2020-11-15-2:2020-11-15-3&Refer=g&page=1',
    #     'https://s.weibo.com/weibo?q=%E5%8F%8C%E5%8D%81%E4%B8%80&scope=ori&suball=1&timescope=custom:2020-11-15-3:2020-11-15-4&Refer=g&page=1',
    #     'https://s.weibo.com/weibo?q=%E5%8F%8C%E5%8D%81%E4%B8%80&scope=ori&suball=1&timescope=custom:2020-11-15-4:2020-11-15-5&Refer=g&page=1',
    #     'https://s.weibo.com/weibo?q=%E5%8F%8C%E5%8D%81%E4%B8%80&scope=ori&suball=1&timescope=custom:2020-11-15-5:2020-11-15-6&Refer=g&page=1',
    #     'https://s.weibo.com/weibo?q=%E5%8F%8C%E5%8D%81%E4%B8%80&scope=ori&suball=1&timescope=custom:2020-11-15-6:2020-11-15-7&Refer=g&page=1',
    #     'https://s.weibo.com/weibo?q=%E5%8F%8C%E5%8D%81%E4%B8%80&scope=ori&suball=1&timescope=custom:2020-11-15-7:2020-11-15-8&Refer=g&page=1',
    #     'https://s.weibo.com/weibo?q=%E5%8F%8C%E5%8D%81%E4%B8%80&scope=ori&suball=1&timescope=custom:2020-11-15-8:2020-11-15-9&Refer=g&page=1',
    #     'https://s.weibo.com/weibo?q=%E5%8F%8C%E5%8D%81%E4%B8%80&scope=ori&suball=1&timescope=custom:2020-11-15-9:2020-11-15-10&Refer=g&page=1',
    #     'https://s.weibo.com/weibo?q=%E5%8F%8C%E5%8D%81%E4%B8%80&scope=ori&suball=1&timescope=custom:2020-11-15-10:2020-11-15-11&Refer=g&page=1',
    #     'https://s.weibo.com/weibo?q=%E5%8F%8C%E5%8D%81%E4%B8%80&scope=ori&suball=1&timescope=custom:2020-11-15-11:2020-11-15-12&Refer=g&page=1',
    #     'https://s.weibo.com/weibo?q=%E5%8F%8C%E5%8D%81%E4%B8%80&scope=ori&suball=1&timescope=custom:2020-11-15-12:2020-11-15-13&Refer=g&page=1',
    #     'https://s.weibo.com/weibo?q=%E5%8F%8C%E5%8D%81%E4%B8%80&scope=ori&suball=1&timescope=custom:2020-11-15-13:2020-11-15-14&Refer=g&page=1',
    #     'https://s.weibo.com/weibo?q=%E5%8F%8C%E5%8D%81%E4%B8%80&scope=ori&suball=1&timescope=custom:2020-11-15-14:2020-11-15-15&Refer=g&page=1',
    #     'https://s.weibo.com/weibo?q=%E5%8F%8C%E5%8D%81%E4%B8%80&scope=ori&suball=1&timescope=custom:2020-11-15-15:2020-11-15-16&Refer=g&page=1',
    #     'https://s.weibo.com/weibo?q=%E5%8F%8C%E5%8D%81%E4%B8%80&scope=ori&suball=1&timescope=custom:2020-11-15-16:2020-11-15-17&Refer=g&page=1',
    #     'https://s.weibo.com/weibo?q=%E5%8F%8C%E5%8D%81%E4%B8%80&scope=ori&suball=1&timescope=custom:2020-11-15-17:2020-11-15-18&Refer=g&page=1',
    #     'https://s.weibo.com/weibo?q=%E5%8F%8C%E5%8D%81%E4%B8%80&scope=ori&suball=1&timescope=custom:2020-11-15-18:2020-11-15-19&Refer=g&page=1',
    #     'https://s.weibo.com/weibo?q=%E5%8F%8C%E5%8D%81%E4%B8%80&scope=ori&suball=1&timescope=custom:2020-11-15-19:2020-11-15-20&Refer=g&page=1',
    #     'https://s.weibo.com/weibo?q=%E5%8F%8C%E5%8D%81%E4%B8%80&scope=ori&suball=1&timescope=custom:2020-11-15-20:2020-11-15-21&Refer=g&page=1',
    #     'https://s.weibo.com/weibo?q=%E5%8F%8C%E5%8D%81%E4%B8%80&scope=ori&suball=1&timescope=custom:2020-11-15-21:2020-11-15-22&Refer=g&page=1',
    #     'https://s.weibo.com/weibo?q=%E5%8F%8C%E5%8D%81%E4%B8%80&scope=ori&suball=1&timescope=custom:2020-11-15-22:2020-11-15-23&Refer=g&page=1',
    #     'https://s.weibo.com/weibo?q=%E5%8F%8C%E5%8D%81%E4%B8%80&scope=ori&suball=1&timescope=custom:2020-11-15-23:2020-11-16-0&Refer=g&page=1',

    # ]
    start_urls = [
        'https://s.weibo.com/weibo?q=%E5%8F%8C%E5%8D%81%E4%B8%80&scope=ori&suball=1&timescope=custom:2020-11-11-4:2020-11-11-5&Refer=g&page=1',
        'https://s.weibo.com/weibo?q=%E5%8F%8C%E5%8D%81%E4%B8%80&scope=ori&suball=1&timescope=custom:2020-11-11-5:2020-11-11-6&Refer=g&page=1'
    ]

    def parse(self,response):

        hasMore = True

        url_parsed = parse.urlparse(response.request.url)
        bits = list(url_parsed)
        qs = parse.parse_qs(bits[4])
        current_page = qs['page'][0]
        current_time = qs['timescope'][0]

        if response.xpath('//div[contains(@class, "card-no-result")]') :
            hasMore = False
        elif response.xpath('//div[contains(@class, "card-wrap")]'):
            dls = response.xpath('//div[contains(@class, "card-wrap")]')
            for dl in dls:
                mid = str(dl.attrib.get('mid'))
                if mid != 'None' :
                    # detailUrl = 'https://m.weibo.cn/detail/'+mid
                    # yield response.follow(detailUrl,callback=self.detailParse)
                    weiboItem = WeiboItem()
                    weiboItem['mblogid'] = mid
                    yield weiboItem
            print(current_time+'----handle page:'+current_page+' finished------')
        else: ## 被认为是机器人或者cookie 失效
            isCaught = True
        

        if hasMore==True:
            try:
                qs['page'] = [str(int(current_page)+1)]
                bits[4] = parse.urlencode(qs,True)
                newUrl = parse.urlunparse(bits)
                yield response.follow(newUrl,callback=self.parse)
            except Exception as error:
                print(error)
        else:
            print(current_time+'-----------finished------')

    def detailParse(self,response):
        try:
            weiboItem = WeiboItem()
            parsed = js2xml.parse(response.xpath('//body/script/text()').extract_first())
            # print(js2xml.pretty_print(parsed))

            mid = parsed.xpath('//property[@name="mid"]/string/text()')[0]
            content = parsed.xpath('//property[@name="text"]/string/text()')[0]
            textLength = parsed.xpath('//property[@name="textLength"]/number/@value')[0]
            source = parsed.xpath('//property[@name="source"]/string/text()')[0]
            userid = parsed.xpath('//property[@name="user"]//property[@name="id"]/number/@value')[0]
            statuses_count = parsed.xpath('//property[@name="user"]//property[@name="statuses_count"]/number/@value')[0]
            nickname = parsed.xpath('//property[@name="user"]//property[@name="screen_name"]/string/text()')[0]
            verified_type = parsed.xpath('//property[@name="user"]//property[@name="verified_type"]/number/@value')[0]
            gender = parsed.xpath('//property[@name="user"]//property[@name="gender"]/string/text()')[0]
            created_at = parsed.xpath('//property[@name="created_at"]/string/text()')[0]
            comments_count = parsed.xpath('//property[@name="comments_count"]/number/@value')[0]
            attitudes_count = parsed.xpath('//property[@name="attitudes_count"]/number/@value')[0]
            reposts_count = parsed.xpath('//property[@name="reposts_count"]/number/@value')[0]
            followers_count = parsed.xpath('//property[@name="followers_count"]/number/@value')[0]
            follow_count = parsed.xpath('//property[@name="follow_count"]/number/@value')[0]

            weiboItem['mblogid'] = mid
            weiboItem['content'] = content
            weiboItem['text_legth'] = textLength
            weiboItem['source'] = source
            weiboItem['user_id'] = userid
            weiboItem['statuses_count'] = statuses_count
            weiboItem['username'] = nickname
            weiboItem['verified_type'] = verified_type
            weiboItem['userGender'] = gender
            weiboItem['created_at'] = created_at
            weiboItem['comment_count'] = comments_count
            weiboItem['attitudes_count'] = attitudes_count
            weiboItem['reposts_count'] = reposts_count
            weiboItem['followers_count'] = followers_count
            weiboItem['friends_count'] = follow_count

            yield weiboItem


        except Exception as error:
            print('main file error')
            print(error)
        finally:
            pass

    