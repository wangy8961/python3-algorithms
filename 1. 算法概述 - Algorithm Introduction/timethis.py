import time
from functools import wraps


def timethis(func):  # 装饰器，输出被装饰的函数的运行时间
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.process_time()
        r = func(*args, **kwargs)
        end = time.process_time()
        print('Function {}() in model {} cost: {} seconds'.format(func.__name__, func.__module__, end - start))
        return r
    return wrapper
