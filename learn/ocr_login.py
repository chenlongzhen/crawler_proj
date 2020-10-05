# 登陆古诗文网
# https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx
import base64

import requests, os, sys
from lxml import etree
from tqdm import tqdm
from PIL import Image

if __name__ == '__main__':

    # gif to png
    def processImage(infile , outfile):
        try:
            im = Image.open(infile)
        except IOError:
            print("Cant load", infile)
            sys.exit(1)
        i = 0
        mypalette = im.getpalette()

        try:
            while 1:
                im.putpalette(mypalette)
                new_im = Image.new("RGBA", im.size)
                new_im.paste(im)
                new_im.save(outfile)

                i += 1
                im.seek(im.tell() + 1)

        except EOFError:
            pass  # end of sequence

    url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}

    response = requests.get(url = url, headers = headers)
    page_text = response.text

    # pic down
    tree = etree.HTML(page_text)
    pic_url = tree.xpath('//div[@class="mainreg2"]/img/@src')[0]
    head_url = 'https://so.gushiwen.cn'
    pic_url = head_url + pic_url

    pic_content = requests.get(url=pic_url, headers = headers).content
    file_dir = 'data'
    file_name = f'{file_dir}/code.gif'
    file_name_png = f'{file_dir}/code.png'

    os.makedirs(file_dir, exist_ok=True)
    with open(file_name, 'wb') as fp:
        fp.write(pic_content)
    # 图片转jpg
    processImage(file_name, file_name_png)


    # pic read
    ## 百度接口
    client_id = 'kDGYtenstQiLSDQRM6tWSUR5'
    client_secret = 'P3NAyI9ce8NVyclNZipX9BWY3XSYVs8X'
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    # https://console.bce.baidu.com/ai/#/ai/ocr/app/detail~appId=1949036
    host = f'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}'
    response = requests.get(host)
    if response:
        access_token = response.json()['access_token']
    else :
        raise("token get error!")
    print(f'access_token: {access_token}')

    # 调用百度 ocr
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
    # 二进制方式打开图片文件
    f = open(file_name_png, 'rb')
    img = base64.b64encode(f.read())

    params = {"image": img}
    access_token = access_token #'[调用鉴权接口获取的token]'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print(response.json())
    f.close()
    code = response.json()['words_result'][0]['words'].strip()
    print(f'识别的验证码为: {code}')

    os.remove(file_name)
    #os.remove(file_name_png)

    # denglu
    session = requests.Session()
    url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
    params={
        '__VIEWSTATE': 'OcCrWS1565UUjsCSZx3wHyz5wgBCJG + Xjv1 + POLngFhmLXY1BrbSRTOOwNWyzWJ7pAZx2ZXtxjWYk79mXlX / laD1FQKW / sJ + dvvNyX3zqNi + P90z4RBytVrXpdA =',
        '__VIEWSTATEGENERATOR': 'C93BE1AE',
        'from': 'http://so.gushiwen.cn/user/collect.aspx',
        'email': '760950023@qq.com',
        'pwd': 'guc521lz',
        'code': code,
        'denglu': '登录'
    }

    response = session.post(url = url, params =params, headers =headers)
    print(response.status_code)
    for cookie in response.cookies:
        print(cookie.name, cookie.value)

    # cookie , 爬取登陆后信息 error
    url = 'https://www.gushiwen.cn/'
    detail_page_text = session.get(url = url).text
    print(detail_page_text)
    tree = etree.HTML(detail_page_text)
    div_list = tree.xpath('//div[@class="cont"]//text()')







