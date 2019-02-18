# 一个字典就是一个键对应一个单值的映射
# 一个键映射多个值需要使用collections 模块中的 defaultdict
from collections import defaultdict

# d = defaultdict(set) 集合无序
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

print(d)
