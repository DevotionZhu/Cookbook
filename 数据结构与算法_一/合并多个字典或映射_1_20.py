# 逻辑上合并为单一的映射，如果出现重复键，那么第一次出现的键值会被返回
from collections import ChainMap
a = {'x':1, 'z':3}
b = {'y':2, 'z':4}
c = ChainMap(a, b)
print(c)
print(c['x'])
print(c['z'])
print(len(c))
print(list(c.keys()))
print(list(c.values()))

