"""
python中单下划线和双下划线：
1.以单下划线开头，表示这是一个保护成员，只有类对象和子类对象自己能访问到这些变量。
2.双下划线开头，表示为私有成员，只允许类本身访问，子类也不行。在文本上被替换为_class__method
"""
class B:
    def __init__(self):
        self.__private =0

    def __private_method(self):
        pass

    def public_method(self):
        pass
        self.__private_method()
# 在前面的类 B 中，私有属性会被分别重命名为 B private 和 B private method

class C(B):
    def __init__(self):
        super().__init__()
        self.__private = 1 # Does not override B.__private
    # Does not override B.__private_method()
    def __private_method(self):
        pass
# 这里，私有名称 private 和 private method 被重命名为 C private 和C private method ，这个跟父类 B 中的名称是完全不同的