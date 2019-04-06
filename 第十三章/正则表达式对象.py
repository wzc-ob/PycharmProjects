import re
r = re.compile('go*d')
#print(r.match('Life can be good'))
print(r.match('Life can be good',14))
print(r.search('Life can be good'))
r = re.compile('b.\sg')
print(r.search('Life can be good'))
r =re.compile('\w.\sg')
print(r.search('Life can be good'))
r= re.compile('\\b\w..?\s')
print(r.findall('Life can be good'))
s= '''Life can be good;
Life can be bad;
Life is mostly cheerful;
But sometimes sad.
'''
r = re.compile('b\w*',re.I)
new = r.sub('*',s)
print(new)
new = r.sub('*',s,2)
print(new)
r = re.compile('b\w*')
new  = r.subn('*',s)
print(new[0])
print(new[1])
new = r.subn('*',s,1)
print(new[0])
print(new[1])
s ='''Life can be good;
Life can be bad;
Life is mostly cheerful;
But somtimes sad.
'''
r = re.compile('\s')
news = r.split(s)
print(news)
news = r.split(s,4)
for i in news:
    print(i)
r= re.compile(r'b\w*',re.I)
news = r.split(s)
print(news)
news = r.split(s,1)
for new in news:
    print(new)
r = re.compile('\w*e',re.I)
news = r.split(s)
print(news)