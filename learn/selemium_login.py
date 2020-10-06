# qq空间登陆
from selenium import webdriver
from time import sleep
import sys
from lxml import etree

# 无头浏览器
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

#规避检测
#https://book.apeland.cn/details/173/
from selenium.webdriver import ChromeOptions
options = ChromeOptions()
options.add_argument('excludeSwitches', ['enable-automation'])

print(sys.path[0])
path = sys.path[0] + '/chromedriver'
# 后面是你的浏览器驱动位置，记得前面加r'','r'是防止字符转义的
driver = webdriver.Chrome(executable_path=path, chrome_options=chrome_options, options=options)

driver.get("https://qzone.qq.com/")
page_text = driver.page_source
print(page_text)
# 切换到frame
driver.switch_to_frame('login_frame')
a_tag = driver.find_element_by_id('switcher_plogin')
a_tag.click()  # 点击

userName_tag = driver.find_element_by_id('u')
password_tag = driver.find_element_by_id('p')
userName_tag.send_keys('xx')
password_tag.send_keys('x')

sleep(0.4)
btn = driver.find_element_by_id('login_button')
btn.click()

sleep(3)
driver.quit()

# TODO :验证条拖动怎么实现?
