# -*- coding: utf-8 -*-
# @Time : 2019/8/29 19:55
# @Author : wangmengmeng
import time
from functools import wraps


def timethis(func):
    @wraps(func)  # 该行代码的目的是避免被装饰函数自身的信息丢失
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wrapper


@timethis
def conutdown(n):
    while n > 0:
        n -= 1
"""
@timethis
def conutdown(n):
    while n > 0:
        n -= 1
等价于 conutdown = timethis(conutdown) 该装饰器代码本身就会运行，而不是等到conutdown(10000)才执行，理解不了的话，在@timethis处打个断点debug一下就知道怎么执行的了
执行过程为：
调用timethis，返回wrapper，且conutdown指向wrapper，所以后面执行conutdown(10000)就相当与执行wrapper(10000)
"""

conutdown(10000)
print(conutdown.__name__)
