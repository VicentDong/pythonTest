from urllib.robotparser import RobotFileParser
from urllib.request import urlopen
from urllib import error
rp = RobotFileParser()
try:
    rp.parse(urlopen('http://www.jianshu.com/robots.txt').read().decode('utf8').split('\n'))
    print(rp.can_fetch('*','http://www.jiansu.com/p/b67554025d7d'))
    print(rp.can_fetch('*','http://www.jianshu.com/search?q=python&age=1&type=collections'))
except error.HTTPError as e :
    print(e.reason)