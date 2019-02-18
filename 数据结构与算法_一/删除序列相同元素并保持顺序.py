# python中hashable概念：python内置的不可变对象都是可哈希的，同时，可变容器 (比如：列表 (list) 或者字典 (dict) ) 都是不可哈希的

# 序列为可hashable类型

def dequpe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dequpe(a)))

# 序列为非hashable类型，如dict
