from lxml import etree
text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html">1 item</a></li>
<li class="item-1"><a href="link2.html">2 item</a></li>
<li class="item-inactive"><a href="link3.html">3 item</a></li>
<li class="item-3"><a href="link4.html">4 item</a></li>
<li class="item-4"><a href="link5.html">5 item</a>
</ul>
</div>
'''
html = etree.HTML(text)
result  = etree.tostring(html)
print(result.decode('utf-8')) 