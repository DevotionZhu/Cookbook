with open(r'somefileName') as somefile:
    for line in somefile:
        print(line)
# 等同于
somefile = open(r'somefileName')
try:
    for line in somefile:
        print(line)
        # ...more code
finally:
    somefile.close()

# with context_expression [as target(s)]:
#     with-body
        # 这里
        # context_expression
        # 当出现with语句的时候，对象的__enter__()方法被触发，它的返回值（如果有的话）会被赋值给as声明的变量
        # target(s) ，如果指定了 as 子句的话，会将上下文管理器的
        # __enter__()
        # 方法的返回值赋值给
        # target(s)。target(s)
        # 可以是单个变量，或者由“()”括起来的元组（不能是仅仅由“, ”分隔的变量列表，必须加“()”）。

