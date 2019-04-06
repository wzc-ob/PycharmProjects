import requests
import urllib.request
from bs4 import BeautifulSoup

imgname =222
def downloadimg(imgurl,imgname):
    saving = open('E:\新建文件夹/'+str(imgname)+'.jpg','wb')
    saving.write(urllib.request.urlopen(imgurl).read())
    saving.close()


def getHTMLText(url):
    try:
        kv = {'user-agent':'Mozilla/5.0'}
        r = requests.get(url,headers = kv,timeout = 30)
        r.raise_for_status()#如果不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"
if __name__ == '__main__':
    url = "https://relifelab.gitlab.io/labreport/"
    soup = BeautifulSoup(getHTMLText(url), 'html.parser')
    # print(soup.prettify())
    for link in soup.find_all('a')[3:-1:2]:
        print(link['href'])
        newsoup = BeautifulSoup(getHTMLText('https://relifelab.gitlab.io'+link['href']),'html.parser')
        for link in newsoup.find_all('img'):
            downloadimg(link['src'],imgname)
            imgname-=1
