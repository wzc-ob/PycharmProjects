import re
s = '''Life can be good;
Life can be bad;
Life is mostly cheerful;
But sometimes sad.
'''
r = re.compile('be(?=\sgood)')
m = r.search(s)
print(m)
print(m.span())
r = re.compile('be')
print(r.findall(s))
r= re.compile('be(?!\sgood)')
m =r.search(s)
print(m)
r= re.compile('(?:can\s)be(\sgood)')
m =r.search(s)
print(m)
print(m.groups())
print(m.group(1))
print(m.group(0))
r = re.compile('(?P<first>\w)(?P=first)')
print(r.findall(s))
r= re.compile(r'(?<=can\s)b\w*\b')
print(r.findall(s))
r= re.compile(r'(?<!can\s)b\w*\b')
print(r.findall(s))
r= re.compile(r'(?<!can\s)(?i)b\w*\b')
print(r.findall(s))


