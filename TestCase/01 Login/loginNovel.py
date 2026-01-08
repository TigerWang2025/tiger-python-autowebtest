import time

from selenium import webdriver
# 打开浏览器
driver = webdriver.Chrome() # 浏览器
# 输入网址
driver.get('http://novel.hctestedu.com/user/login.html')

time.sleep(5)
driver.quit()