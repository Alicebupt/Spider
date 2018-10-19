# -*- coding: utf-8 -*-

# Scrapy settings for zhihu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhihu'

SPIDER_MODULES = ['zhihu.spiders']
NEWSPIDER_MODULE = 'zhihu.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'

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
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
	"authority": "www.zhihu.com",
	":method": "GET",
	":path": "/api/v4/members/liuyu-43-97/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=60&limit=20",
	":scheme": "https",
	"accept": "*/*",
	"accept-language": "zh-CN,zh;q=0.9",
	"cookie": "_zap=d85df9b5-b2fb-48d4-9494-25b6c123a3eb; __DAYU_PP=a22a33mabZMyMzInuBF33246518de440; d_c0=AJBmkmLD5A2PTm9EGL6HqmAsXpyL2Zev8hY=|1531470339; _xsrf=e5DwuLHjCrc28C7azh4ivJFO1gRNLhKQ; capsion_ticket=2|1:0|10:1539047841|14:capsion_ticket|44:NzU5NTViMDUwOWUxNGE4Njg1NzFiMzU1ODI3ZDJmZWU=|4aee1ad8b65ce74bd79cfa509be10cdb5ca39ab2b95997c62acbf42e11776fe2; z_c0=2|1:0|10:1539047927|4:z_c0|92:Mi4xaTVsMkF3QUFBQUFBa0dhU1lzUGtEU2NBQUFDRUFsVk45NDdqV3dDazFTYjhmTmtrSlozSTg3b0VKaVFNN1A0SW9R|e945925e3a9e3b80256afee874681c2af94642a8fbe80d401deb83544c6aa5e6; q_c1=8504c918c50c422c952c567c7f25b73c|1539047927000|1520919290000; __utma=51854390.1251691535.1539047983.1539047983.1539047983.1; __utmz=51854390.1539047983.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.100--|2=registration_date=20160917=1^3=entry_date=20160917=1; tgw_l7_route=8605c5a961285724a313ad9c1bbbc186; tst=r",
	"referer": "https://www.zhihu.com",
	"x-requested-with": "fetch",
	"x-udid": "AJBmkmLD5A2PTm9EGL6HqmAsXpyL2Zev8hY=",
	"x-zse-83": "3_1.1",
	"x-zse-84": "kwrlNc_kKw8bTkrlgg9k0GKk90bv9dQkzhAl0D_lMsubQsbm1pAlLSolRseb8prk"
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zhihu.middlewares.ZhihuSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'zhihu.middlewares.ZhihuDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'zhihu.pipelines.ZhihuPipeline': 300,
#}

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
