# -*- coding: utf-8 -*-

# Scrapy settings for csdn_crawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

COMMANDS_MODULE = 'csdn_crawler.commands'

BOT_NAME = 'csdn_crawler'

SPIDER_MODULES = ['csdn_crawler.spiders']
NEWSPIDER_MODULE = 'csdn_crawler.spiders'

LOG_LEVEL = 'INFO'
LOG_FILE = './log.log'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'csdn_crawler (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
  'Accept-Language': 'en',
  'Cookie': "JSESSIONID=1043A7B9DAD64D4EA1B2C21C93D964F5; TY_SESSION_ID=e4520256-c9ab-4253-876e-42ccb78fbdf3; uuid_tt_dd=10_21018060000-1556443950416-891396; dc_session_id=10_1556443950416.467541; _ga=GA1.2.1973651575.1558672008; UM_distinctid=16ae835a30711d-0fde6e9d09e44d-3764460c-100200-16ae835a30860; acw_tc=2760820715698073555523036e3d026e43b7e434d70073de07cfea47734761; __yadk_uid=TykbqapWsDf0eDSAbMSTYQiTgbQvvtiu; UserName=qq_36269019; UserInfo=de64f808f654470c81d6a590bc0f2abc; UserToken=de64f808f654470c81d6a590bc0f2abc; UserNick=qq_36269019; AU=A47; UN=qq_36269019; BT=1569823119138; p_uid=U000000; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=6525*1*10_21018060000-1556443950416-891396!1788*1*PC_VC!5744*1*qq_36269019; smidV2=201910081405317f100b100d80c77946fde70357e5ef7100c021de3572d0510; __gads=Test; firstDie=1; announcement=%257B%2522isLogin%2522%253Atrue%252C%2522announcementUrl%2522%253A%2522https%253A%252F%252Fblogdev.blog.csdn.net%252Farticle%252Fdetails%252F102605809%2522%252C%2522announcementCount%2522%253A0%252C%2522announcementExpire%2522%253A3600000%257D; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1572234956,1572310186,1572310421,1572310938; dc_tos=q044fk; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1572312946",
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'

}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'csdn_crawler.middlewares.CsdnCrawlerSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'csdn_crawler.middlewares.CsdnCrawlerDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'csdn_crawler.pipelines.CsdnCrawlerPipeline': 300,
   'csdn_crawler.pipelines.MysqlPipeline': 301,
   'csdn_crawler.pipelines.HtmlSqlPipeline': 302,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
