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
