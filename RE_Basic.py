# difference between group() and group()
import re
str = 'ab'
m = re.match('ab',str)
print m.group()   # 'ab'
print m.groups()  #  None

m = re.match('(a)(b)',str)
print m.group()   # 'ab'
print m.groups()  # ('a','b')

m = re.search('(a)(b)',str)
print m.group()   # 'ab'
print m.group()   # ('a','b')
m = re.finall('(a)(b)',str)
print m # [('a','b')]
