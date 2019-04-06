import requests
import re
from bs4 import BeautifulSoup

def downloadtext(i,alllist):
    saving = open('E:\新建文件夹/'+str(alllist) + '.txt', 'a+', encoding='UTF-8')
    saving.write(i)
    saving.write('\n')
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
    url = "http://www.quanshuwang.com/book/135/135941"
    soup = BeautifulSoup(getHTMLText(url), 'html.parser')
    for link in soup.find_all('a')[21:22]:
        newsoup = BeautifulSoup(getHTMLText(link['href']),'html.parser')
        for i in newsoup.find_all(string = re.compile('(.*?)')):
            downloadtext(i,link['title'])
