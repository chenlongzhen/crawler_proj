# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os

from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
from riverProj.dingding import send_dingding_msg
import scrapy
# TODO: from scrapy.pipelines.media import MediaPipeline
from scrapy.settings import Settings
from scrapy.utils.misc import md5sum
from scrapy.utils.python import to_bytes
from io import BytesIO

from itemadapter import ItemAdapter
from PIL import Image

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
        imgName = f'./imgs/{title}/' + url.split('/')[-1].replace("_gzip.aspx","")
        print(imgName)
        return imgName

    # https://blog.csdn.net/php_fly/article/details/19688595
    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        return item  # 返回给下一个即将被执行的管道类
    # https://www.24fa.cc/upload/2020-09/200922173782963.jpg_gzip.aspx

#    def image_downloaded(self, response, request, info, *, item=None):
#        checksum = None
#        for path, image, buf in self.get_images(response, request, info, item=item):
#            if checksum is None:
#                buf.seek(0)
#                checksum = md5sum(buf)
#            width, height = image.size
#            self.store.persist_file(
#                path, buf, info,
#                meta={'width': width, 'height': height},
#                headers={'Content-Type': 'image/jpeg'})
#        return checksum
#
#    def get_images(self, response, request, info, *, item=None):
#        path = self.file_path(request, response=response, info=info)
#        orig_image = Image.open(BytesIO(response.body))
#        print(f"path: {path}")
#        print(orig_image)
#
#        width, height = orig_image.size
#        if width < self.min_width or height < self.min_height:
#            raise ("Image too small "
#                                 f"({width}x{height} < "
#                                 f"{self.min_width}x{self.min_height})")
#
#        image, buf = self.convert_image(orig_image)
#        yield path, image, buf
#
#        for thumb_id, size in self.thumbs.items():
#            thumb_path = self.thumb_path(request, thumb_id, response=response, info=info)
#            thumb_image, thumb_buf = self.convert_image(image, size)
#            yield thumb_path, thumb_image, thumb_buf
#
#    def convert_image(self, image, size=None):
#        if image.format == 'PNG' and image.mode == 'RGBA':
#            background = Image.new('RGBA', image.size, (255, 255, 255))
#            background.paste(image, image)
#            image = background.convert('RGB')
#        elif image.mode == 'P':
#            image = image.convert("RGBA")
#            background = Image.new('RGBA', image.size, (255, 255, 255))
#            background.paste(image, image)
#            image = background.convert('RGB')
#        elif image.mode != 'RGB':
#            image = image.convert('RGB')
#
#        if size:
#            image = image.copy()
#            image.thumbnail(size, Image.ANTIALIAS)
#
#        buf = BytesIO()
#        image.save(buf, 'JPEG')
#        return image, buf
