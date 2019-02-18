def spam(a, b=42):
    print(a, b)


spam(1)
spam(1, 2)

# 默认参数的值仅在函数定义时赋值一次
x = 34
def sp(a, b=x):
    print(a, b)
x=23
sp(1)
sp(1)

