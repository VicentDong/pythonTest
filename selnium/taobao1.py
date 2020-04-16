from selenium import webdriver

broswer = webdriver.Chrome()
broswer.get('http://www.taobao.com')

lists  = broswer.find_elements_by_css_selector('.service-bd li')
print(lists)
broswer.close()