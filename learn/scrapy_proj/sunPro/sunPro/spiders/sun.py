import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from sunPro.items import SunproItem, DetailItem

class SunSpider(CrawlSpider):
    name = 'sun'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://wz.sun0769.com/political/index/politicsNewest?id=1&page=1']

    link = LinkExtractor(allow=r'id=\d+&page=\d+')
    link_detail = LinkExtractor(allow=r'politics/index\?id=\d+')
    rules = (
        Rule(link, callback='parse_item', follow=True),
        Rule(link_detail, callback='parse_detail')
    )

    custom_settings = {
        'DOWNLOAD_DELAY': 6
    }

    def parse_item(self, response):
        # tbody标签不能出现!
        li_list = response.xpath('/html/body/div[2]/div[3]/ul[2]/li')
        for li in li_list:
            item = SunproItem()
            item['title'] = li.xpath('./span[3]//text()').extract_first()
            item['new_num'] = li.xpath('./span[1]/text()').extract_first()

            yield item

    def parse_detail(self, response):
        div = response.xpath('//div[@class="mr-three"]')
        item = DetailItem()
        item['new_id'] = div.xpath('./div[1]/span[4]/text()').extract_first()
        item['content'] = div.xpath('./div[2]/pre/text()').extract_first()
        yield item
