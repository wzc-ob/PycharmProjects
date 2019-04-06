import re
s = '''Life can be dreams,
Life can be great thoughts;
Life can mean a person,
Sitting in a court.'''
r = re.compile('\\b(?P<first>\w+)a(\w+)\\b')
m = r.search(s,9)
print(m.start())
print(m.start(1))
print(m.start(2))
print(m.end(1))
print(m.end())
print(m.span())
print(m.span(2))