from functools import wraps
from random import randint


def log(str_template=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if str_template:
                print(str_template.format(randint(10, 100)))
            else:
                # default template
                print(f'{func.__name__} took {randint(10,100)} seconds')
            return result
        return wrapper
    return decorator
