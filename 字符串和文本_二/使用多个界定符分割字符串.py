import re
line = 'asdf fjdk; afed, fjek,asdf, foo'
print(re.split(r'[;,\s]\s*', line)) # 分隔符可以是逗号，分号或者是空格，并且后面紧跟着任意个的空格