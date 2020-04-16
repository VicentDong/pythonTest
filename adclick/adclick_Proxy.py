#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import threading
from time import sleep, ctime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
# 引入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import urllib.parse
import urllib.request
from lxml import etree

# 初始化点击次数
global clickTotalTimes
clickTotalTimes = 10
# 成功次数
global clickTimes
clickTimes = 0
global user_agent_list
user_agent_list = ['Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0']

def getProxy():
    url = "http://p.ashtwo.cn/"
    user_agent = user_agent_list[0]
    headers = {'User-Agent': user_agent_list[0]}
    req = urllib.request.Request(url=url, headers=headers)
    res = urllib.request.urlopen(req)
    content = res.read()
    proxyIPAndPort = etree.HTML(content).xpath(
        '/html/body/p/text()')
    return proxyIPAndPort[0]


def CheckProxyIsCorrect(proxy):

    proxy_support = urllib.request.ProxyHandler(
        {'http': r'http://'+proxy})
    opener = urllib.request.build_opener(
        proxy_support, urllib.request.HTTPHandler)
    opener.addheaders = [("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.168 Safari/537.36")]
    url = 'http://httpbin.org/ip'
    try:
        response = opener.open(url, timeout=10)
        html = response.read()
        if html:
            return True
        else:
            return False
    except urllib.error.HTTPError as e:
        # print('CheckProxyIsCorrect:', proxy, ' HTTPError:', e)
        return False
    except urllib.error.URLError as e:
        # print('CheckProxyIsCorrect:', proxy, ' URLError:', e)
        return False
    except Exception as e:
        # print('CheckProxyIsCorrect:', proxy, ' Exception:', e)
        return False
    finally:
        sleep(3)


# 模拟点击


def activeClick():

    global clickTimes

    # 获取可用代理
    isProxyAble = False
    while isProxyAble == False:
        proxy = getProxy()
        # proxy = '120.210.219.102:8080'
        isProxyAble = CheckProxyIsCorrect(proxy)
        sleep(3)

    chromeOptions = Options()
    # 无头模式
    # chromeOptions.add_argument('--headless')
    # 设置代理 一定要注意，=两边不能有空格，不能是这样--proxy-server = http://202.20.16.82:10152
    chromeOptions.add_argument("--proxy-server=http://"+proxy)
    # 使用chrome
    driver = webdriver.Chrome(chrome_options=chromeOptions)

    # 全屏
    driver.maximize_window()
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
              " end " + ctime()+", Error:" + str(e))
    finally:
        driver.quit()
        sleep(3)

# proxy test


def testProxyDriver():

    global clickTimes

    isProxyAble = False
    while isProxyAble == False:
        proxy = getProxy()
        isProxyAble = CheckProxyIsCorrect(proxy)
        sleep(1)

    chromeOptions = Options()
    # 无头模式
    chromeOptions.add_argument('--headless')
    # 设置代理 一定要注意，=两边不能有空格，不能是这样--proxy-server = http://202.20.16.82:10152
    chromeOptions.add_argument("--proxy-server=http://"+proxy)
    # 使用chrome
    driver = webdriver.Chrome(chrome_options=chromeOptions)

    # 全屏
    driver.maximize_window()
    # 设置浏览器地址
    driver.get('https://www.baidu.com')
    # 设置隐式等待为10秒
    driver.implicitly_wait(5)

    try:
        # 模拟滚动条滚动
        js = "var q=document.documentElement.scrollTop=" + str(800)
        driver.execute_script(js)

        # 定位到要悬停的元素
        above = driver.find_element_by_xpath(
            "//*[@id='su']")
        # 对定位到的元素执行鼠标悬停操作
        ActionChains(driver).move_to_element(above).perform()

        search = driver.find_element_by_id("su")
        search.click()

        print("click times: " + str(clickTimes) + " end " + ctime())
        clickTimes = clickTimes + 1
    except NoSuchElementException as e:
        print("click times: " + str(clickTimes) +
              " end " + ctime()+", Error:" + str(e))
    finally:
        driver.quit()
        sleep(3)


if __name__ == "__main__":
    while clickTimes < clickTotalTimes:
        print("click times: " + str(clickTimes) + " begining " + ctime())
        activeClick()
        # testProxyDriver()
