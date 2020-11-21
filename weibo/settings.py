# Scrapy settings for weibo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'weibo'

SPIDER_MODULES = ['weibo.spiders']
NEWSPIDER_MODULE = 'weibo.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'weibo (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False
# COOKIES_DEBUG = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
  'Cache-Control': 'no-cache',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Cookie': 'UM_distinctid=1757909379b610-053c67b4db414-3971095d-1fa400-1757909379c46d; SINAGLOBAL=1211125594811.8083.1604053449062; UOR=,,www.google.com; ALF=1636807539; SUB=_2A25yquXHDeRhGeRI7lQQ9i3Pwz-IHXVuVIuPrDV8PUJbkNANLVXikW1NUrGMMm13NZthXCz_SQ6BP6lKx8tbz5PM; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFw8TmAGHvC23gRuTFkJ6iR5NHD95QESo-ceKq0e0n0Ws4Dqcjci--Xi-zRiKyWi--fi-zRiKL2i--Xi-ihiKLWi--ciKyWiK.fi--4i-8Wi-z7i--fi-82iK.7; wvr=6; _s_tentry=-; Apache=4689775633844.188.1605333939547; ULV=1605333939595:3:2:2:4689775633844.188.1605333939547:1605091797133; webim_unReadCount=%7B%22time%22%3A1605339254426%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A66%2C%22chat_group_notice%22%3A1%2C%22allcountNum%22%3A81%2C%22msgbox%22%3A0%7D; WBStorage=8daec78e6a891122|undefined',
  'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'weibo.middlewares.WeiboSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'weibo.middlewares.WeiboDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'weibo.pipelines.WeiboPipeline': 300,
}
MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'weibo'
MYSQL_USER = 'weibo'
MYSQL_PASSWD = 'weibo'
MYSQL_PORT = 3306

LOG_LEVEL = "INFO"
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
