#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
from lxml import etree
import time
import random
import re
def reg(html):
    reg = r"(<div class='ie-fix'>)(.+?)(.+?)(</p></div>)"
    all = re.compile(reg)
    alllist = re.findall(all, html)
    print(alllist)
    return alllist[0][3]
# url = "http://www.27270.com/tag/267.html"
# url = "http://www.baidu.com"
url = 'https://wenku.baidu.com/view/fad8f54d657d27284b73f242336c1eb91a3733e7.html'
html_bytes = urllib.request.urlopen(url).read()
# print(html_bytes)
html = html_bytes.decode("gb2312")
# page = etree.HTML(html.lower())
# img_src =page.xpath('*//img/@src')
# img_src = page.xpath('//text')
# print(img_src)

#     time.sleep(random.randint(5,20))