import requests
r = requests.get('http://httpbin.org/get?name=haha&age=22')
print(r.text)
print(type(r.text))
print(r.json())
print(type(r.json()))

import re
headers={
    'User-Agent': 'Mozilla/4.0 (Mozilla/5.0 (Macintosh; Inter Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
r =requests.get('http://www.zhihu.com/explore',headers=headers)
# pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)
pattern = re.compile('ExploreSpecialCard-contentTag(.*?)</a>',re.S)
titles = re.findall(pattern,r.text)
print(titles)