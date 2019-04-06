import urllib.request
import re
def reg(html):
    reg = r'({"img":")(.+?)(","title)'
    all  = re.compile(reg)
    alllist = re.findall(all,html)
    print(alllist)
    return alllist
url = 'http://www.tybai.com/'
html_bytes = urllib.request.urlopen(url).read()
html = html_bytes.decode("UTF-8")
print(html)
imgurls = reg(html)
print(imgurls)
imgname = 1
for imgurl in imgurls:
    print(imgurl[1])
    # saveimg = open("E:/" + str(imgname) + ".jpg", 'wb')
    newimgurl = 'http://www.tybai.com/'+imgurl[1].replace('\\','')
    savingimg = open('E:/'+str(imgname)+'.jpg','wb')
    savingimg.write(urllib.request.urlopen(newimgurl).read())
    savingimg.close()
    imgname+=1

