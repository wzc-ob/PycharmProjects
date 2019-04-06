from lxml import etree
import urllib.request
url = 'http://www.tybai.com/'
html_byts = urllib.request.urlopen(url).read()
html =html_byts.decode('UTF-8')
page= etree.HTML(html.lower())
