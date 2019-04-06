import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r= requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillUninList(ulist,html):
    soup =BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string])

def printUnivList(ulist,num):
    tplt = "{0:^10}\t{1:{4}^10}\t{2:^10}\t{3:^10}"
    print("{0:^6}\t{1:{4}^10}\t{2:^10}\t{3:^10}".format("排名","学校名称","地理位置","总分",chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0],u[1],u[2],u[3],chr(12288)))
def main():
    uinfo = []
    url = "http://www.zuihaodaxue.com/shengyuanzhiliangpaiming2016.html"
    html = getHTMLText(url)
    fillUninList(uinfo,html)
    printUnivList(uinfo,50)

main()
