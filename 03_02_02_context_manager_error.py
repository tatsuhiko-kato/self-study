class MyOpenContextManager:
    '''MyOpenContextManager
    '''
    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        print('__enter__: ファイルをopenします')
        self.file_obj = open(self.file_name, 'r')
        return self.file_obj
    
    def __exit__(self, type, value, traceback):
        print(f'__exit__(type): {type}')
        print(f'__exit__(value): {value}')
        print(f'__exit__(traceback): {traceback}')
        print('__exit__: ファイルをcloseします')
        self.file_obj.close()

with MyOpenContextManager('python.txt') as f:
    print(f.read())
    raise ValueError('my context manager error')