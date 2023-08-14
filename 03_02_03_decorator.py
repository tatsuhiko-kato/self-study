import contextlib
import traceback
@contextlib.contextmanager
def my_open_context_manager(file_name):
    '''my_open_context_manager
    '''
    file_obj = open(file_name, 'r')
    try:
        print('__enter__: ファイルをopenします')
        yield file_obj
    except Exception as e:
        print(f'__exit__: {type(e)} ')
        print(f'__exit__: {e}')
        print(f'__exit__: {list(traceback.TracebackException.from_exception(e).format())}')
        raise
    finally:
        file_obj.close()
        print('__exit__: ファイルをcloseします')

with my_open_context_manager('python.txt') as f:
    print(f.read())
