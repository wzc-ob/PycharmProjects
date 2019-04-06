import re
s = 'Life can be good'
print(re.match('can',s)   )
print(re.search('can',s))
print(re.match('1.*',s))
print(re.match('l.*',s,re.I))
print(re.findall('[a-z]{3}',s))
print(re.findall('[a-z]{1,3}',s))
s= 'Life can be bad'
#print(re.sub('bad','good',s))
#print(re.sub('bad|be','good',s))
#print(re.sub('bad|be','good',s,1))
print(re.subn('bad|be','good',s,1))
r = re.subn('bad|be','good',s)
print(r[0])
print(r[1])
s = 'Life can be bad'
print(re.split(' ',s))
print(re.split(' ',s,1))
print(re.split('b',s))
