# Scrapy settings for riverProj project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'riverProj'

SPIDER_MODULES = ['riverProj.spiders']
NEWSPIDER_MODULE = 'riverProj.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

#LOG_LEVEL = "INFO"
#LOG_FILE = "mySpider.log"

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'riverProj.middlewares.RiverprojSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'riverProj.middlewares.RiverprojDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'riverProj.pipelines.RiverprojPipeline': 300,
}

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

#pic 目录
IMAGES_STORE='./data'

# 通过在settings.py中设置DEPTH_LIMIT的值可以限制爬取深度，这个深度是与start_urls中定义url的相对值。也就是相对url的深度。例如定义url为：http://www.domz.com/game/,DEPTH_LIMIT=1那么限制爬取的只能是此url下一级的网页。深度大于设置值的将被ignore。
#如果为零（默认），则不从深度进行优先级调整
#正值将降低优先级，即，较高深度请求将被稍后处理 ; 这通常用于做广度优先爬网（BFO）
#负值将增加优先级，即，较高深度请求将被更快地处理（DFO）
DEPTH_LIMIT =  3
DEPTH_PRIORITY = 3
DEPTH_STATS_VERBOSE = True #深度状态收集

# 避免下载最近90天已经下载过的文件内容
FILES_EXPIRES = 90
# 避免下载最近90天已经下载过的图像内容
IMAGES_EXPIRES = 30

## 设置图片缩略图
#IMAGES_THUMBS = {
#    'small': (50, 50),
#    'big': (250, 250),
#}
# 图片过滤器，最小高度和宽度，低于此尺寸不下载
IMAGES_MIN_HEIGHT = 110
IMAGES_MIN_WIDTH = 110