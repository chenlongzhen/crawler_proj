# 配置
```
 - 创建一个工程：scrapy startproject xxxPro
    - cd xxxPro
    - 在spiders子目录中创建一个爬虫文件
        - scrapy genspider spiderName www.xxx.com 
        - scrapy genspider -t crawl xxx www.xxxx.com # crawlspider 用于全站爬取
    - 执行工程：
        - scrapy crawl spiderName
    - settings.py配置 
    ```
    # Obey robots.txt rules
    ROBOTSTXT_OBEY = False
    LOG_LEVEL = 'ERROR'
    ```
```
# 代理
[csdn:设置代理的三种方式](https://blog.csdn.net/weixin_38091140/article/details/96454326?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param)

# 中间件
```python
#middlewares.py
# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


from scrapy.http import HtmlResponse
from time import sleep
class WangyiproDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.



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
    #该方法拦截五大板块对应的响应对象，进行篡改
    def process_response(self, request, response, spider):#spider爬虫对象
        bro = spider.bro#获取了在爬虫类中定义的浏览器对象

        #挑选出指定的响应对象进行篡改
        #通过url指定request
        #通过request指定response
        if request.url in spider.models_urls:
            bro.get(request.url) #五个板块对应的url进行请求
            sleep(3)
            page_text = bro.page_source  #包含了动态加载的新闻数据

            #response #五大板块对应的响应对象
            #针对定位到的这些response进行篡改
            #实例化一个新的响应对象（符合需求：包含动态加载出的新闻数据），替代原来旧的响应对象
            #如何获取动态加载出的新闻数据？
                #基于selenium便捷的获取动态加载数据
            new_response = HtmlResponse(url=request.url,body=page_text,encoding='utf-8',request=request)

            return new_response
        else:
            #response #其他请求对应的响应对象
            return response



    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

```

# PIPELINE 保存
```python
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os

from itemadapter import ItemAdapter
import pymysql


class QiubaiproPipeline:
    def open_spider(self, spider):
        '''
        重写父类方法, 只被调用一次
        :param spider:
        :return:
        '''
        print('mysql: begin scrapy in open_spider')
        os.makedirs('./data', exist_ok=True)
        self.fp = open('./data/qiubai.txt','w',encoding='utf-8')

    def process_item(self, item, spider):
        author = item['author']
        content = item['content']

        self.fp.write(f"{author}: {content}\n")
        return item

    def close_spider(self,spider):
        '''

        :param spider:
        :return:
        '''
        self.fp.close()
        print(f'结束爬虫!')

# 存到数据库
class mysqlPileLine(object):
    conn = None
    cursor = None
    def open_spider(self,spider):
        self.conn = pymysql.Connect(host='127.0.0.1',port=3306,user='root',password='123456',db='qiubai',charset='utf8')
    def process_item(self,item,spider):
        self.cursor = self.conn.cursor()

        try:
            self.cursor.execute('insert into qiubai values("%s","%s")'%(item["author"],item["content"]))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

        return item
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()

```
## 图片
```python
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class ImgsproPipeline(object):
#     def process_item(self, item, spider):
#         return item
from scrapy.pipelines.images import ImagesPipeline
import scrapy
class imgsPileLine(ImagesPipeline):

    #就是可以根据图片地址进行图片数据的请求
    def get_media_requests(self, item, info):

        yield scrapy.Request(item['src'])

    #指定图片存储的路径
    def file_path(self, request, response=None, info=None):
        imgName = request.url.split('/')[-1]
        return imgName

    def item_completed(self, results, item, info):
        return item #返回给下一个即将被执行的管道类


```