import pymongo 
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse  import quote
from pyquery import PyQuery as pq


MAX_PAGE = 100
KEYWORD = 'iPad'

MONGO_URL = 'localhost'
MONGO_DB ='taobao'
MOGO_COLLECTION = 'products'

client = pymongo.MongoClient(MONGO_URL) 
db = client[MONGO_DB]
broswer = webdriver.Chrome()
wait = WebDriverWait(broswer,10)

def index_page(page):
    print('正在爬取第',page,'页')
    try:
        url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
        broswer.get(url)
        if page > 1:
            input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager div.form > input')))
            submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR,'#mainsrp-pager div.form > span.btn.J_Submit'))
            )
            input.clear()
            input.send_keys(page)
            submit.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#miansrp-pager li.item.active > span'),str(page)))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.m-itemlist .items .item')))
        get_products()
    except TimeoutException:
        index_page(page)

def get_products():
    html = broswer.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item  in items:
        product = {
            'image': item.find('.pic .img').attr('data-src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text(),
            'title':item.find('.title').text(),
            'shop':item.find('.shop').text(),
            'location':item.find('.location').text()
        }
        print(product)
        save_to_mongo(product)



def save_to_mongo(result):
    try:
        if db[MOGO_COLLECTION].insert(result):
            print('存储到MongoDB成功')
    except Exception:
        print('存储到MongoDB失败')




def main():
    for i in range(1,MAX_PAGE + 1):
        index_page(i)



if __name__ == '__main__':
    main()