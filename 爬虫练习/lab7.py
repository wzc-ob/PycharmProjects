import requests
r = requests.get('https://s.taobao.com/search?q=书包&s=0')
r.encoding = r.apparent_encoding
print(r.text)
print(r.raise_for_status())