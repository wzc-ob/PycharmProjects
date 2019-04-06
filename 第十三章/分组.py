import re
s= 'Phone No. 010-87654321'
# r = re.compile('(\d+)-(\d+)')
# m = r.search(s)
# print(m)
# print(m.group(1))
# print(m.group(2))
# print(m.groups())
r = re.compile('(?P<Area>\d+)-(?P<No>\d+)')
m = r.search(s)
print(m)
print(m.groupdict())
print(m.group('No'))
print(m.group('Area'))