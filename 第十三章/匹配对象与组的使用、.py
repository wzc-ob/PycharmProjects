import re
s = '''Life can be dreame,
Life can be great thoughts;
Life can mean a person,
Sitting in a court.'''
r= re.compile('\\b(?P<first>\w+)a(\w+)\\b')
m = r.search(s)
print(m)
print(m.groupdict())
print(m.groups())
m =r.search(s,9)
print(m.group())
print(m.group(1))
print(m.group(2))
print(m.group(1,2))
print(m.groupdict())
print(m.groups())