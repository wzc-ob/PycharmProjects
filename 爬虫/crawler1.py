#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.request
# url = "http://www.tybai.com/static/jpg/1.jpg"
url = "http://www.baidu.com"

html_bytes = urllib.request.urlopen(url).read()
html = html_bytes.decode("UTF-8")

import re
def reg(html):
    reg = r'(<marquee)(.+?)(>)(.+?)(</marquee>)'
    all = re.compile(reg)
    alllist = re.findall(all,html)
    return alllist[0][3]
print(html)
