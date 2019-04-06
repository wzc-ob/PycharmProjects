import re
import urllib.request
import requests
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
         }
# url = 'http://www.quanshuwang.com/book/44/44683/15379612.html'
url = 'http://www.quanshuwang.com/book/0/567/7347707.html'

#http://www.quanshuwang.com/book/44/44683/15380196.html
def reg(html):
    reg =r'&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />'
    return re.findall(reg,html)

def download(url):
    try:
        return requests.get(url=url,headers=header)
    except IOError as e:
        print('失败')
    return requests.get(url=url,headers=header)

html_byts = download(url)
# html_byts.content.decode('UTF-8')
html = html_byts.content.decode('GBK')
# print(html)
# print(reg(html))
alllist = reg(html)
saving = open(str(alllist[0])+'.txt','w',encoding='UTF-8')
for i in alllist:
    print(i)
    saving.write(i)
    saving.write('\n')
saving.close()

