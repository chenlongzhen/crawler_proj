import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from riverProj.items import RiverprojItem


class MeimvSpider(CrawlSpider):
    name = 'meimv'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.24fa.cc/c49p1.aspx']

    domain_link = LinkExtractor(allow=r'c49p\d+\.aspx')
    detail_link = LinkExtractor(allow=r'n\d+c\d+[p\d+]{0,}\.aspx')
    rules = (
        Rule(domain_link, callback='parse_item', follow=False),
        Rule(detail_link, callback='parse_detail', follow=False),
    )

    def parse_item(self, response):
        print('1')
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
        print(img_list)
        for img_content in img_list:

            title = img_content.xpath('./div[1]/h1/text()').extract_first()
            img_url_list = img_content.xpath('./div[3]//img/@src').extract() # img url列表

            for img_url in img_url_list:
                item = RiverprojItem()
                item['title'] = title
                item['img_url'] = r'http://www.24fa.cc/' +  img_url
                yield item
