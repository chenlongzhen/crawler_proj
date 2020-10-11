import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from riverProj.items import RiverprojItem
from scrapy.utils.log import configure_logging
import logging

class MeimvSpider(CrawlSpider):
    name = 'meimvxxx'
    allowed_domains = ['www.24fa.cc']
    start_urls = [f'https://www.24fa.cc/c49p{i}.aspx' for i in range(1,2,1)]
    #start_urls = [f'https://www.24fa.cc/n58135c49.aspx' for i in range(1,2,1)]

    #domain_link = LinkExtractor(allow=r'c49p\d+\.aspx')
    detail_link1 = LinkExtractor(allow=r'n\d+c49[p\d+]{0,1}\.aspx')
    #detail_link2 = LinkExtractor(allow=r'n\d+c49[p\d+]{1,1}\.aspx')
    rules = (
    #    Rule(domain_link, callback='parse_item', follow=False),
        Rule(detail_link1, callback='parse_detail', follow=False),
    #    Rule(detail_link2, callback='parse_detail', follow=False),
    )
    # 打印到文件，zaisetting中设置打印到文件 终端就没有了
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

            sub_url_list = img_content.xpath('./table//tr/td/div/ul/li/a/@href').extract()
            title = img_content.xpath('./div[1]/h1/text()').extract_first()
            img_url_list = img_content.xpath('//*[@id="printBody"]/div[3]/div[1]/div[contains(@style,"text-align")]/img/@src').extract() # img url列表 #tbody不要 # //尽量少来做比较精确的匹配

            # 调过一张图的页面
            if len(img_url_list) < 2:
                continue

            for img_url in sub_url_list:
                url = r'http://www.24fa.cc/' + img_url
                yield scrapy.Request(url=url, callback=self.parse_detail)

            for img_url in img_url_list:
                item = RiverprojItem()
                item['title'] = title
                item['img_url'] = r'http://www.24fa.cc/' +  img_url
                yield item
