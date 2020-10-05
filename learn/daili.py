
import requests
url = 'https://www.baidu.com/s?wd=ip'
proxies = {'https':'60.179.231.216:3000'} # 需要确认这个ip是http 还是https的
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}

page_text = requests.get(url = url, headers = headers, proxies = proxies).text
#page_text = requests.get(url = url, headers = headers).text

with open('ip.html','w',encoding='utf-8') as fp:
    fp.write(page_text)