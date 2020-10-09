#encoding=utf-8

import requests

url = 'https://www.24fa.cc/upload/2020-09/200922173782963.jpg_gzip.aspx'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
}
response = requests.get(url = url, headers = headers)

with open('./test.jpg', 'wb') as fp:
    fp.write(response.content)

