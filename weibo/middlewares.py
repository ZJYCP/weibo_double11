# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class WeiboSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class WeiboDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None
        # request.cookie={
        #       'UM_distinctid':'1757909379b610-053c67b4db414-3971095d-1fa400-1757909379c46d',
        #       'SINAGLOBAL':'1211125594811.8083.1604053449062',
        #       'UOR':',,www.google.com',
        #       'ALF':'1636807539',
        #       'SUB':'_2A25yquXHDeRhGeRI7lQQ9i3Pwz-IHXVuVIuPrDV8PUJbkNANLVXikW1NUrGMMm13NZthXCz_SQ6BP6lKx8tbz5PM',
        #       'SUBP':'0033WrSXqPxfM725Ws9jqgMF55529P9D9WFw8TmAGHvC23gRuTFkJ6iR5NHD95QESo-ceKq0e0n0Ws4Dqcjci--Xi-zRiKyWi--fi-zRiKL2i--Xi-ihiKLWi--ciKyWiK.fi--4i-8Wi-z7i--fi-82iK.7',
        #       'wvr':'6',
        #       '_s_tentry':'-',
        #       'Apache':'4689775633844.188.1605333939547; ULV=1605333939595:3:2:2:4689775633844.188.1605333939547:1605091797133',
        #       'webim_unReadCount':'%7B%22time%22%3A1605339254426%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A66%2C%22chat_group_notice%22%3A1%2C%22allcountNum%22%3A81%2C%22msgbox%22%3A0%7D',
        #       'WBStorage':'8daec78e6a891122|undefined'
        # }
        # return request

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
