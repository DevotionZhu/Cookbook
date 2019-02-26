# pthon 定义了__str__()和__repr__()两种方法，__str__()用于显示给用户，而__repr__()用于显示给开发人员
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __repr__(self):
        return 'Pair({0.x!r},{0.y!r})'.format(self)
    def __str__(self):
        return '(Person: %s, %s)' % (self.name, self.gender)
p = Person('Bob', 'male')
print(p)

# 特别来讲，
# !r 格式化代码指明输出使用 repr () 来代替默认的 str () .示例：
# >>> p = Pair(3, 4)
# >>> print('p is {0!r}'.format(p))
# p is Pair(3, 4)
# >>> print('p is {0}'.format(p))
# p is (3, 4)
