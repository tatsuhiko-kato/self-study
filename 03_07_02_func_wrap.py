def my_wrapper(func):
    '''my_wrapper
    '''
    def wrap_function():
        func()
        print(f'function: {func.__name__} called')

    return wrap_function
    
def greeting():
    '''greeting
    '''
    print('こんにちは')

greeting = my_wrapper(greeting)
greeting()
