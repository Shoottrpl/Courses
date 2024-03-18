from  functools import wraps
import math

def df_decorator(dx=0.01):
    def func_decorator(func):
        @wraps(func)
        def wraper(x, *args, **kwargs):
            res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
            return res
        #wraper.__name__ = func.__name__
        #wraper.__doc__ = func.__doc__

        return wraper
    return func_decorator

@df_decorator(dx=0.1)
def sin_df(x):
    """Функция для вычисления производного синуса"""
    return math.sin(x)

print(sin_df.__name__)
print(sin_df.__doc__)
