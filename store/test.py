import requests
from pyquery import PyQuery as pq

url = 'https://www.zhihu.com/explore'

headers ={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}

html = requests.get(url,headers=headers).text
doc = pq(html)
items = doc('.ExploreHomePage-specials .ExploreSpecialCard').items()
for item in items:
    question = item.find('.ExploreSpecialCard-contentTitle').text()
    file = open('explore.txt','a',encoding='utf-8')
    file.write('\n'.join([question]))
    file.write('\n' + '='*50 + '\n')
    file.close()