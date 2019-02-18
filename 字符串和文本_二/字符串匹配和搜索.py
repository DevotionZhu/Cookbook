import re

# 方法一：调用基本字符串方法，如str.find(),str.endwith(),str.startwith()
# 方法二：对于复杂的匹配需要使用正则表达式和 re 模
text = 'yeah, but no, but yeah, but no, but yeah'
print(text.startswith('yeah'))
print(text.endswith('no'))
print(text.find('no'))

# 如果想使用同一个模式去做多次匹配，应该先将模式字符串预编译为模式对象
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

datepat = re.compile(r'\d+/\d+/\d+')   # \d+ means match one or more digits
if datepat.match(text1):
    print('yes')
else:
    print('no')

