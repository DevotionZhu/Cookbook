# 通过zip()函数将字典“反转”为（值，键）

price = {'AAA': 777,'ZZZ':888}
print(min(zip(price.values(), price.keys())))
print(max(zip(price.values(), price.keys())))