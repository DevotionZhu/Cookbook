from decimal import Decimal

# 浮点数不能精确的表达十进制数
a = 4.2
b = 2.1
print(a + b)  # output:6.300000000000001

c = Decimal('4.2')
d = Decimal('2.1')
print(c + d) # output: 6.3