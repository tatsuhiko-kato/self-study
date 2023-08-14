def my_decorator(func):
    def wrap_function():
        func()
        print(f'function: {func.__name__} called')
    return wrap_function

@my_decorator
def greeting():
    print('こんにちは')

greeting()
