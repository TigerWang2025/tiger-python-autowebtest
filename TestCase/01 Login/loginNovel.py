import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 打开浏览器
driver = webdriver.Chrome() # 浏览器
# 输入网址
driver.get('http://novel.hctestedu.com/user/login.html')

# 用户名：15096268001 ，密码： 123456
# 使用Xpath ，输入用户名
driver.find_element(By.XPATH, '//*[@id="txtUName"]').send_keys('15096268001')
# 使用id ，输入密码
driver.find_element(By.ID, 'txtPassword').send_keys('123456')
# 使用name，查找按钮，点击按钮
driver.find_element(By.NAME, 'btnLogin').click()


time.sleep(5)
driver.quit()