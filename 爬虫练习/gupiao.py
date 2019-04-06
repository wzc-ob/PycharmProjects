import re
import requests
from bs4 import BeautifulSoup
import traceback
def getHTMLText(url,code = 'UTF-8'):
    try:
        kv = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=kv, timeout=30)
        r.encoding = code
        # print(r.text)
        return r.text
    except:
        return ""

def getStockList(lst,stockURL):
   html = getHTMLText(stockURL,'GB2312')
   soup = BeautifulSoup(html,'html.parser')
   a = soup.find_all('a')
   for i in a:
       try:
           href = i.attrs['href']
           lst.append(re.findall(r'[s][hz]\d{6}',href)[0])
       except:
           continue


def getStockInfo(lst,stockURL,fpath):
    count = 0
    for stock in lst:
        url = stockURL +stock +".html"
        print(url)
        html = getHTMLText(url)
        try:
            if html =='':
                continue
            infoDict = {}
            soup = BeautifulSoup(html,'html.parser')
            stockInfo = soup.find('div',attrs={'class':'stock-bets'})
            name = stockInfo.find_all(attrs = {'class':'bets-name'})[0]
            print(name.text.split()[0])
            infoDict.update({'股票名称':name.text.split()[0]})

            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val
            with open(fpath,'a',encoding='UTF-8') as f:
                f.write(str(infoDict) +'\n')
                count = count+1
                print('\r当前进度：{:.2f}%'.format(count*100/len(lst)),end='')
        except:
            traceback.print_exc()
            continue

def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_file = 'E://BaiduStockInfo(1).txt'
    slist = []
    getStockList(slist,stock_list_url)
    getStockInfo(slist,stock_info_url,output_file)

main()