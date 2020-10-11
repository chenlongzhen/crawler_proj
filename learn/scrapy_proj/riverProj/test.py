#encoding=utf-8

import requests
from lxml import etree

"""
url = 'https://www.24fa.cc/upload/2020-09/200922173782963.jpg_gzip.aspx'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
}
response = requests.get(url = url, headers = headers)

with open('./test.jpg', 'wb') as fp:
    fp.write(response.content)
"""

url = "http://www.24fa.cc/n77745c49p2.aspx"

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
}
response = requests.get(url = url, headers = headers)

page_text = response.text

# 实例化
tree = etree.HTML(page_text)
# r = tree.xpath('/html/body/div[5]/div[5]/div[1]/ul/li')

li_list = tree.xpath('//*[@id="printBody"]/div[3]/div[1]/div[contains(@style,"text-align")]/img/@src')
#li_list = tree.xpath('//*[@id="dlNews"]//tr')
print(li_list)

for li in li_list:
    #c = li.xpath('.//a/@href')
    print(li)
