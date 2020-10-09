# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os

from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
import scrapy

class ImgsPipeline(object):
    def process_item(self, item, spider):
        return item

class RiverprojPipeline(ImagesPipeline):
    #content可以用,区别是什么?
    #https://www.jianshu.com/p/6f508d29b6d5
    # 就是可以根据图片地址进行图片数据的请求
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['img_url'],meta = {"item": item}) # meta传参

    # 指定图片存储的路径
    def file_path(self, request, response=None, info=None):
        item = request.meta["item"]
        title = item.get('title')
        url = item.get('img_url')
        os.makedirs(f'./imgs/{title}', exist_ok=True)
        imgName = f'./imgs/{title}/' + url.split('/')[-1]
        print(imgName)
        return imgName
    # https://blog.csdn.net/php_fly/article/details/19688595
    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        return item  # 返回给下一个即将被执行的管道类
    # https://www.24fa.cc/upload/2020-09/200922173782963.jpg_gzip.aspx