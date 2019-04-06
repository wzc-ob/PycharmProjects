import requests
kv = {'wd':'Python'}
r = requests.get('http://www.baidu.com/s',params=kv)
print(r.status_code)
print(r.request.url)
print(len(r.text))

path = 'E:/abc.jpg'
url = 'https://img10.360buyimg.com/imgzone/jfs/t17605/227/1164909166/40732/d31a7999/5abf1b9aN5bfcc800.jpg'
r = requests.get(url)
with open(path,'wb') as f:
    f.write(r.content)
