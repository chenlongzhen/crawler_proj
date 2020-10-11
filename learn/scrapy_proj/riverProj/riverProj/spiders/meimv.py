import scrapy
from riverProj.items import RiverprojItem
from scrapy.utils.log import configure_logging
import logging

class MeimvSpider(scrapy.Spider):
    name = 'meimv'
    allowed_domains = ['www.24fa.cc']
    start_urls = [f'https://www.24fa.cc/c49p{i}.aspx' for i in range(1,2,1)]

    # 打印到文件，zaisetting中设置打印到文件 终端就没有了
    configure_logging(install_root_handler=False)
    logging.basicConfig(
        filename='log.txt',
        format='%(levelname)s: %(message)s',
        level=logging.INFO
    )

    def parse(self, response):
        """
        first page
        :param response:
        :return:
        """
        img_title_list = response.xpath('//*[@id="dlNews"]//tr')
        # fixme
        for img_title in img_title_list:
            img_url = img_title.xpath('.//a/@href').extract_first()
            url = r'http://www.24fa.cc/' + img_url
            yield scrapy.Request(url=url, callback=self.parse_detail)

    def parse_detail(self, response):
        """
        每个图组页为第一页爬取 并且将其他页抽取给下一步parse 抽取其他图片
        :param response:
        :return:
        """
        img_list = response.xpath('//*[@id="printBody"]')

        for img_content in img_list:
            title = img_content.xpath('./div[1]/h1/text()').extract_first()
            img_url_list = img_content.xpath(
                '//*[@id="printBody"]/div[3]/div[1]/div[contains(@style,"text-align")]/img/@src').extract()  # img url列表 #tbody不要 # //尽量少来做比较精确的匹配
            sub_url_list = img_content.xpath('./table//tr/td/div/ul/li/a/@href').extract()

            if len(img_url_list) < 2:
                continue

            for img_url in img_url_list:
                item = RiverprojItem()
                item['title'] = title
                item['img_url'] = r'http://www.24fa.cc/' + img_url
                yield item

            # 其他页
            for img_url in sub_url_list:
                url = r'http://www.24fa.cc/' + img_url
                yield scrapy.Request(url=url, callback=self.parse_detail_v2)

    def parse_detail_v2(self, response):
        img_list = response.xpath('//*[@id="printBody"]')

        for img_content in img_list:
            title = img_content.xpath('./div[1]/h1/text()').extract_first()
            img_url_list = img_content.xpath(
                '//*[@id="printBody"]/div[3]/div[1]/div[contains(@style,"text-align")]/img/@src').extract()  # img url列表 #tbody不要 # //尽量少来做比较精确的匹配

            if len(img_url_list) < 2:
                continue

            for img_url in img_url_list:
                item = RiverprojItem()
                item['title'] = title
                item['img_url'] = r'http://www.24fa.cc/' + img_url
                yield item

    def extract_item(self,img_content):
        """
        抽取图片url
        :param img_content:
        :return:
        """
        title = img_content.xpath('./div[1]/h1/text()').extract_first()
        img_url_list = img_content.xpath(
            '//*[@id="printBody"]/div[3]/div[1]/div[contains(@style,"text-align")]/img/@src').extract()  # img url列表 #tbody不要 # //尽量少来做比较精确的匹配
        sub_url_list = img_content.xpath('./table//tr/td/div/ul/li/a/@href').extract()
        if len(img_url_list) < 2:
            return []

        return img_url_list

