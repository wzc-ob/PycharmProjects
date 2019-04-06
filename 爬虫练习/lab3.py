import requests
from bs4 import BeautifulSoup
url = 'https://python123.io/ws/demo.html'
r= requests.get(url)
soup = BeautifulSoup(r.text,'html.parser')
# print(soup.prettify())
print(soup.title)
tag = soup.a
print(tag)
print(tag.attrs)
print(tag.attrs['href'])
print(soup.a.parent.name)