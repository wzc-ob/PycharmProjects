import requests
import re
from bs4 import BeautifulSoup
url = 'https://python123.io/ws/demo.html'
r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser')
# print(soup.prettify())
for link in soup.find_all('a'):
    print(link['href'])
print(soup.find_all(string = re.compile('python')))
