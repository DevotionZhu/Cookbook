import random
values = [1, 2, 3, 4, 5]
# 随机抽取一个元素
print(random.choice(values))
# 提取N个不同元素
print(random.sample(values, 2))
# 打乱序列中元素的顺序
random.shuffle(values)
print(values)