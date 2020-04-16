from urllib.robotparser import RobotFileParser
rp = RobotFileParser()
rp.set_url('http://www.jianshu.com/robots.txt')
rp.read()
print(rp.can_fetch('*','http://www.jiansu.com/p/b67554025d7d'))
print(rp.can_fetch('*','http://www.jianshu.com/search?q=python&age=1&type=collections'))
