import scrapy


class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    # allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        divs = response.xpath('//div[contains(@class,"col1 old-style-col1")]/div')
        for div in divs:
            author = div.xpath('./div[1]/a[2]/h2/text()')[0]
            content = div.xpath('./a[1]/div/span//text()') # 有其他子标签用//text()!!

            # extract or extract_first
            #print(author.extract().strip()) # 将selector中的data对象提取
            #print("".join(content.extract()).replace(" ","").strip())
            #print('======')

             ##############################
             # 基于管道, 指令的方式见资料代码
             ##############################



    ##############################
    # user agent 也需要在setting中配置
    ##############################
