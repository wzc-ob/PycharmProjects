import requests

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
    url = "https://python123.io/ws/demo.html"
    print(getHTMLText(url))