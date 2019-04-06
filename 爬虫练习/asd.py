import re
import urllib.request
import requests
url = 'http://www.521609.com/'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
         }
print

html_byts = requests.get(url = url,headers = header)

html =  html = html_byts.content.decode('GBK')
newimgurl = 'http://www.521609.com/uploads/allimg/151126/1-151126144I90-L.jpg'
saving = open('1.jpg','wb')
saving.write(urllib.request.urlopen(newimgurl).read())
saving.close()
# print(html)