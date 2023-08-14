import contextlib
from time import time, sleep
@contextlib.contextmanager
def timed(func_name):
    start = time()
    try:
        yield
    finally:
        end = time()
        print(f'{func_name}: (total: {end - start})')

with timed('sleep processing'):
    sleep(2)