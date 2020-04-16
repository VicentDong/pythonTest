from selenium import webdriver

broswer = webdriver.Chrome()
broswer.get('http://www.taobao.com')
input_first = broswer.find_element_by_id('q')
input_second = broswer.find_element_by_css_selector('#q')
input_third = broswer.find_element_by_xpath('//*[@id="q"]')
print(input_first,input_second,input_third)
broswer.close()