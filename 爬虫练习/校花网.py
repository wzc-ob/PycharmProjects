import re
import urllib.request
import requests
import threading
threadpool = []

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
         }

def reg(html):
    #/uploads/allimg/140717/1-140GF92J7-lp.jpg
    #/uploads/120503/1_122F3340.jpg
    reg1 = r'/uploads/allimg/\d+/.*\.jpg'
    reg2 = r'/uploads/\d+/.*\.jpg'
    # reg = r'\d+/.*\.jpg'
    return re.findall(reg1,html)+re.findall(reg2,html)

def downloadimg(imgurl,imgname):
    newimgurl = 'http://www.521609.com' + imgurl
    print(newimgurl)
    saving = open(str(imgname)+'.jpg','wb')
    saving.write(urllib.request.urlopen(newimgurl).read())
    saving.close()


def download(url):
    try:
        return requests.get(url=url,headers=header)
    except IOError as e:
        print('失败')
    return requests.get(url=url,headers=header)
imgname =1
for i  in range(32,358):
    url =  'http://www.521609.com/daxuexiaohua/list%s.html'%i
    # print(url)
    html_byts = download(url)
    # print(html_byts)
    html = html_byts.content.decode('GBK','ignore')
    # print(html)
    print(reg(html))
    imgurls = reg(html)

    for imgurl in imgurls:
        downloadimg(imgurl,imgname)
        # th = threading.Thread(target=downloadimg,args=(imgurl,imgname))
        # threadpool.append(th)
        imgname+=1
    # print(threadpool)
# for th1 in threadpool:
    # th1.start()
# for th1 in threadpool:
    # th1.join()

