class Date:
    __slots__ = ['year', 'month', 'day']
    def __init__(self, year, month, day):
        self.yaer = year
        self.month = month
        self.day  = day

'''
    当你定义 slots 后， Python 就会为实例使用一种更加紧凑的内部表示。实例通
过一个很小的固定大小的数组来构建，而不是为每个实例定义一个字典，这跟元组或
列表很类似。在 slots 中列出的属性名在内部被映射到这个数组的指定小标上。使
用 slots 一个不好的地方就是我们不能再给实例添加新的属性了，只能使用在 slots
中定义的那些属性名
'''