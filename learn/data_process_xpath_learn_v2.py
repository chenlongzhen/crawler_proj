# 图片

import requests, os
from lxml import etree
from tqdm import tqdm

if __name__ == "__main__":
    url = 'http://pic.netbian.com/4kmeinv'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}

    # 使用通用爬虫对url对应的整个页面爬取
    response = requests.get(url=url, headers=headers)
    # 手动设定编码格式,可能不好使
    # response.encoding = 'utf-8'
    page_text = response.text

    # 实例化
    tree = etree.HTML(page_text)
    # r = tree.xpath('/html/body/div[5]/div[5]/div[1]/ul/li')
    li_list = tree.xpath('//ul[@class="clearfix"]/li')

    file_dir = 'data/pic_data'
    os.makedirs(file_dir, exist_ok=True)

    head_url = 'http://pic.netbian.com'
    for li in tqdm(li_list):
        pic_url = li.xpath('./a/@href')[0]
        pic_url = head_url + pic_url
        pic_name = li.xpath('./a/img/@alt')[0]
        pic_name = pic_name.encode('iso-8859-1').decode('gbk')  # 乱码需要处理
        pic_name = pic_name.replace(' ', '')[:30]

        # 图片down
        pic_text = requests.get(url=pic_url, headers=headers).text
        tree = etree.HTML(pic_text)
        pic_url_detail = tree.xpath('//div[@class="photo-pic"]/a/img/@src')[0]
        pic_url_detail = head_url + pic_url_detail

        pic_content = requests.get(pic_url_detail, headers=headers).content

        with open(file_dir + f"/{pic_name}{pic_url_detail[-4:]}", 'wb') as fp:
            fp.write(pic_content)
        print(f"save {pic_name}")
