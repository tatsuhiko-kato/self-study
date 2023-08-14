# self-study
# 3 Pythonの言語仕様
## 3.2 with文
### 3.2.1 with文

<details>
<summary>
with文を使用する例 ※python.txtを開いて読み込む
</summary>

```python
with open('python.txt') as f:
    f.read()
```
</details>

<details>
<summary>
with文を使用しない例
</summary>

```python
f = None
try:
    f = open('python.txt')
    print(f.read())
finally:
    if f:
        f.close()
```
</details>

### 3.2.2 コンテキストマネージャー
<details>
<summary>
ファイルオブジェクトのメソッドを確認
</summary>

```python
file_obj = open('python.txt')
file_dir = dir(file_obj)
'__enter__' in file_dir
# True
'__exit__' in file_dir
# True
```
</details>

<details>
<summary>
コンテキストマネージャーの作成 ※ファイルをopenして中身を表示し、closeする
</summary>

```python
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
        print('__exit__: ファイルをcloseします')
        self.file_obj.close()

with MyOpenContextManager('python.txt') as f:
    print(f.read())
'''
__enter__: ファイルをopenします
Python!
__exit__: ファイルをcloseします
'''
```
</details>

<details>
<summary>
with ブロック内で例外発生
</summary>

```python
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
'''
__enter__: ファイルをopenします
Python!
__exit__(type): <class 'ValueError'>
__exit__(value): my context manager error
__exit__(traceback): <traceback object at 0x7fe187bb6000>
__exit__: ファイルをcloseします
Traceback (most recent call last):
  File "/workspaces/self-study/03_02_02_context_manager_error.py", line 21, in <module>
    raise ValueError('my context manager error')
ValueError: my context manager error
```
</details>

### 3.2.3 標準ライブラリのデコレーター
<details>
<summary>
MyOpenContextManagerクラスと同等のコンテキストマネージャーを実装
</summary>

```python
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
'''
__enter__: ファイルをopenします
Python!
__exit__: ファイルをcloseします
'''
```
</details>

### 3.2.4 with文：よくある使い方
<details>
<summary>
処理の実行時間を計測するコンテキストマネージャー
</summary>

```python
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

'''
sleep processing: (total: 2.001443862915039)
'''
```
</details>