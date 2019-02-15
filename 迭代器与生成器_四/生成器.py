from collections.abc import Generator
# 迭代器，是在可迭代的基础上，加了一个next()方法
# 生成器，则是在迭代器的基础上（可以用for循环，可以使用next()），再实现了yield

# 创建生成器有两个方法：1.使用列表生成是2.实现yield的方法
# 使用列表生成式，注意不是[]，而是()
L = (x * x for x in range(10))
print(isinstance(L, Generator))  # True
# 实现yield的函数
def mygen(n):
    now = 0
    while now < n:
        yield now
        now += 1

if __name__ == '__main__':
    gen = mygen(10)
    print(isinstance(gen, Generator))  # True
# 由于生成器并不是一次生成所有元素，而是一次一次的执行返回，那么如何刺激生成器执行(或者说激活)呢？
# 激活主要有两个方法
# 使用next()
# 使用generator.send(None)


def mygen(n):
    now = 0
    while now < n:
        yield now
        now += 1


if __name__ == '__main__':
    gen = mygen(4)

    # 通过交替执行，来说明这两种方法是等价的。
    print(gen.send(None))
    print(next(gen))
    print(gen.send(None))
    print(next(gen))




