# -*- coding: utf-8 -*-
# @Time : 2019/8/29 19:55
# @Author : wangmengmeng
import time
from functools import wraps


def timethis(func):
    @wraps(func)
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


conutdown(10000)
