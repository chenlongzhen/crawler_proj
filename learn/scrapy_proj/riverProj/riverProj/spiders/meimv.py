import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from riverProj.items import RiverprojItem
from scrapy.utils.log import configure_logging
import logging

class MeimvSpider(CrawlSpider):
    name = 'meimv'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.24fa.cc/c49p1.aspx']

    domain_link = LinkExtractor(allow=r'c49p\d+\.aspx')
    detail_link = LinkExtractor(allow=r'n\d+c\d+[p\d+]{0,}\.aspx')
    rules = (
        Rule(domain_link, callback='parse_item', follow=True),
        Rule(detail_link, callback='parse_detail', follow=True),
    )

    configure_logging(install_root_handler=False)
    logging.basicConfig(
        filename='log.txt',
        format='%(levelname)s: %(message)s',
        level=logging.INFO
    )

    def parse_item(self, response):
        #print('1')
        pass
        # https://www.24fa.cc/c49.aspx
        #tr_list = response.xpath('//*[@id="dlNews"]//tr')
        #for tr in tr_list:
        #    td_list = tr.xpath('./td')
        #    for td in td_list:
        #        detail_url = td.xpath('./a/@href').extract_first()
        #        pic_url= td.xpath('./a/@src').extract_first().replace('_gzip.aspx','')
        #        title = td.xpath('./a/@alt').extract_first()
        #        #pic_url = r'http://www.24fa.cc/'

    def parse_detail(self, response):

        img_list = response.xpath('//*[@id="printBody"]')
        #print(img_list)
        for img_content in img_list:

            title = img_content.xpath('./div[1]/h1/text()').extract_first()
            img_url_list = img_content.xpath('./div[3]/div[contains(@class,"text-align")]/img/@src').extract() # img url列表 #tbody不要 # //尽量少来做比较精确的匹配

            for img_url in img_url_list:
                item = RiverprojItem()
                item['title'] = title
                item['img_url'] = r'http://www.24fa.cc/' +  img_url
                yield item
