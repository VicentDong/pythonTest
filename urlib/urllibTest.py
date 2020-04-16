from urllib import request,parse
# import  socket
# import urllib.request
# import urllib.error
# import urllib.parse
# response = urllib.request.urlopen('https://www.python.org')
# # print(response.read().decode('utf-8'))
# # print(type(response))
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))
# data  = bytes(urllib.parse.urlencode({'world':'hello'}),encoding='utf8')
# response = urllib.request.urlopen('http://httpbin.org/get',timeout=1)
# print(response.read())
# try:
#     response = urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
# except urllib.error.URLError as e:
#     if  isinstance(e.reaso,socket.timeout):
#         print('TIME OUT')

# 使用opener
url = 'http://httpbin.org/post'
headers={
    'User-Agent':'Mozilla/4.0 (compatible;MSIE 5.5;Windows NT)',
    'Host':'httpbin.org'
}
dict = {
    'name':'Germey'
}
data = bytes(parse.urlencode(dict),encoding='utf8')
req = request.Request(url=url,data=data,headers=headers,method='POST')
req.add_header('User-Agent','Mozilla/4.0 (compatible;MSIE 5.5;Windows NT)')
response = request.urlopen(req)
print(response.read().decode('utf-8'))
