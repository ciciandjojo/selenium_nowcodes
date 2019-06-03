from selenium import webdriver
import time
#导入Keys 模块，然后我们看看Keys 模块定义了那些按键
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(r"C:\Users\Administrator\Downloads\chromedriver.exe")
browser.get("https://www.nowcoder.com/login")

inputUserElement = browser.find_element_by_id('jsEmailIpt')
inputPasswordElement = browser.find_element_by_id('jsPasswordIpt')
searchButton = browser.find_element_by_id("jsLoginBtn")

#账号和密码填自己的账号密码
inputUserElement.send_keys("账号")
inputPasswordElement.send_keys("密码")
searchButton.click()
time.sleep(2)

#登录成功后
sousuoElement = browser.find_element_by_class_name("js-search-btn")
sousuoElement.click()
time.sleep(1)
inputSearchElement = browser.find_element_by_class_name("nav-search-txt")
inputSearchElement.send_keys("京东")
inputSearchElement.send_keys(Keys.ENTER)

#点击查看更多
findMoreElement = browser.find_elements_by_class_name('link-green')[1]
findMoreElement.click()
time.sleep(2)

#查看更多后


UlElement = browser.find_element_by_class_name("common-list")
num = 0
for i in UlElement.find_elements_by_class_name("discuss-detail"):
    if num > 4:
        break
    else:
        ji = i.text.replace(u'\U0001f411', '')
        print(i.text)
        num = num + 1
        time.sleep(1)

