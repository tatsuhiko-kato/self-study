import sys

def print_hello():
    print('Hello!')


sys.breakpointhook = print_hello


if __name__ == '__main__':
    print('start')
    breakpoint()
    print('end')