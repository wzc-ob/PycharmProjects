import urllib.request
from lxml import etree
import requests
import threading
from concurrent.futures import ThreadPoolExecutor
# url = 'http://search.smzdm.com/?c=home&s=rimowa'
# header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',
#           'Referer': 'http://search.smzdm.com/?c=home&s=rimowa',
#           'Host': 'search.smzdm.com'}

# url = 'http://blog.csdn.net/eric_sunah/article/details/11099295'
# header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',
#           'Referer': 'http://blog.csdn.net/eric_sunah/article/details/11099295',
#           'Host': 'blog.csdn.net'}

urls = ['http://www.27270.com/tag/267.html','http://www.27270.com/tag/267_2.html','http://www.27270.com/tag/267_3.html']
# url = 'http://www.27270.com/ent/meinvtupian/'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
         }
threadpool =[]

def downloadimg(imgurl,imgname):
    saving = open('E:\爬虫图片\httpwww.27270.comentmeinvtupian\学生/' + str(imgname) + '.jpg', 'wb')
    saving.write(urllib.request.urlopen(imgurl).read())
    saving.close()
    print(imgname)

# html_byts = urllib.request.urlopen(url).read()
# html = html_byts.decode('UTF-8')
imgname = 0
pool = ThreadPoolExecutor(max_workers=100)
for url in urls:
    html_byts = requests.get(url=url,headers=header)
    html = html_byts.content.decode('gb2312')
# print(html)

    page = etree.HTML(html.lower())
    img_src =page.xpath('*//img/@src')
    print(img_src)
    # print(img_src)
    # saving = open('E:/second.jpg','wb')
    # imgurl = 'http://qny.smzdm.com/201711/24/5a17740b34d5d3237.jpg_d200.jpg'
    # imgurl = 'http://search.smzdm.com/?c=home&s=rimowa'+img_src[0]

    for imgurl in img_src:
        th = threading.Thread(target=downloadimg,args=(imgurl,imgname))
        # downloadimg()
        threadpool.append(th)
        imgname += 1
    print(threadpool)
for th in threadpool:
    th.start()
for th in threadpool:
    th.join()

    # for imgurl in img_src:
    #     # th = threading.Thread(target=downloadimg,args=(imgurl,imgname))
    #     # downloadimg()
    #     pool.submit(downloadimg(imgurl,imgname))
    #     # threadpool.append(th)
    #     imgname += 1