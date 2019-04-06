import re
import urllib.request
import requests
import threading

threadpool = []
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
         }
url = 'http://www.quanshuwang.com/book/44/44683'
# url ='http://www.quanshuwang.com/book/22/22573'
#http://www.quanshuwang.com/book/44/44683/15380196.html
def reg(html):
    reg =r'(http://www.quanshuwang.com/book/44/44683/\d+\.html)(" title=")(.*?)共'
    # reg =r'(http://www.quanshuwang.com/book/44/44683/\d+\.html)(" title=")([\u4e00-\u9fa5]{7})'

    return re.findall(reg,html)

def reg2(html):
    reg =r'&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />'
    return re.findall(reg,html)
def download(url):
    try:
        return requests.get(url=url,headers=header)
    except IOError as e:
        print('失败')
    return requests.get(url=url,headers=header)

def downloadtext(i,alllist):
    saving = open(str(alllist[0]) + '.txt', 'a+', encoding='UTF-8')
    saving.write(i)
    saving.write('\n')
    saving.close()

html_byts = download(url)
htmls = html_byts.content.decode('GBK')
x =1
for html in reg(htmls):
    print(x)
    url = html[0]
    html_byts = download(url)
    html = html_byts.content.decode('GBK')
    alllist = reg2(html)

    x+=1
    for i in alllist:
        downloadtext(i,alllist)
        # print(i)
        th = threading.Thread(target=downloadtext, args=(i, alllist[0]))
        threadpool.append(th)
for th in threadpool:
    th.start()
for th in threadpool:
    th.join()


