import re
r = re.compile('[1-9]([0-9]{5,11})')
print(r.findall('2690465376'))