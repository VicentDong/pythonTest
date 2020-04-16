#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import threading
from time import sleep, ctime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
# 引入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains

# 初始化点击次数
global clickTotalTimes
clickTotalTimes = 60
# 成功次数
global clickTimes
clickTimes = 0


# 模拟点击
def activeClick():
    global clickTimes

    chromeOptions = webdriver.ChromeOptions()
    # 无头模式
    chromeOptions.add_argument('--headless')
    # 设置代理 一定要注意，=两边不能有空格，不能是这样--proxy-server = http://202.20.16.82:10152
    # chromeOptions.add_argument("--proxy-server=http://"+proxy)
    # 使用chrome
    driver = webdriver.Chrome(chrome_options=chromeOptions)

    # 全屏
    # driver.maximize_window()
    # 设置浏览器地址
    driver.get('https://ad.doubleclick.net/ddm/clk/444343793;248016268;n')

    # 设置隐式等待为10秒
    driver.implicitly_wait(5)

    try:
        # 模拟滚动条滚动
        js = "var q=document.documentElement.scrollTop=" + str(800)
        driver.execute_script(js)

        # 定位到要悬停的元素
        above = driver.find_element_by_xpath(
            "//*[@id='gwp']/div/div[1]/div/div/dl/dd/a/img")
        # 对定位到的元素执行鼠标悬停操作
        ActionChains(driver).move_to_element(above).perform()

        if clickTimes%4 == 0:
            store1 = driver.find_element_by_id("GWP_CDFG")
            ActionChains(driver).click(store1)
        elif clickTimes%4 == 1:
            store2 = driver.find_element_by_id("GWP_Lotte")
            ActionChains(driver).click(store2)
        elif clickTimes%4 == 2:
            store3 = driver.find_element_by_id("GWP_Shilla")
            ActionChains(driver).click(store3)
        elif clickTimes%4 == 3:
            store4 = driver.find_element_by_id("GWP_SSG")
            ActionChains(driver).click(store4)

        print("click times: " + str(clickTimes) + " end " + ctime())
        clickTimes = clickTimes + 1
    except NoSuchElementException as e:
        print("click times: " + str(clickTimes) +
              " end "+ctime()+", Error:" + str(e))
    finally:
        driver.quit()
        sleep(3)



# 多线程
if __name__ == "__main__":
    while clickTimes < clickTotalTimes:
        print("click times: " + str(clickTimes) + " begining " + ctime())
        activeClick()
