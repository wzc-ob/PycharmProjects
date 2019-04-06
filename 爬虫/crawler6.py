import urllib.request
from lxml import etree
import requests
import time
import random
url = "https://www.baidu.com/s?"
# postdata={
# '_'	:'1520952605926',
#     'ie':'utf-8',
#     'wd':'TTyb|个人网站'
# }
keyword = input('请输入你要搜索的关键词：')
def getnowtime():
    timerandom = random.randint(100,999)
    nowtime = int(time.time())
    nowtime+timerandom

postdata={
'_'	:getnowtime(),
    'ie':'utf-8',
    'wd':keyword#'TTyb|个人网站'
}

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
         }
html_byts = requests.get(url,headers=header,params=postdata)
html = html_byts.content.decode("UTF-8",'ignore')
print(html)
