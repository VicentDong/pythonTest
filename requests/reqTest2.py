import requests
r =requests.get('http://github.com/favicon.ico')
# print(r.text)
# print(r.content)
with open('favicon.icon','wb') as f:
    f.write(r.content)