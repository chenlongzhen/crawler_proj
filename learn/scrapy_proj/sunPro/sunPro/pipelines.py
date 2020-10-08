# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os

from itemadapter import ItemAdapter


class SunproPipeline:

    def open_spider(self, spider):
        '''
        重写父类方法, 只被调用一次
        :param spider:
        :return:
        '''
        print('begin scrapy pipeline')
        os.makedirs('./data', exist_ok=True)
        self.fp = open('./data/title.txt','w',encoding='utf-8')
        self.fp2 = open('./data/content.txt','w',encoding='utf-8')

    def process_item(self, item, spider):
        # 如何判定item的类型
        # 将数据写入数据库时，如何保证数据的一致性
        #print(item)
        if item.__class__.__name__ == 'DetailItem':
            self.fp2.write(f"{item['new_id']}\t{item['content']}\n")
        else:
            self.fp.write(f"{item['title']}\t{item['new_num']}\n")
        return item

    def close_spider(self,spider):
        '''
        :param spider:
        :return:
        '''
        self.fp.close()
        self.fp2.close()
        print(f'结束爬虫!')