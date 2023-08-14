# self-study
# 3 Pythonの言語仕様
## 3.7 デコレーター
### 3.7.1 デコレーターを使用する

### 3.7.2 関数デコレーターを自作する
<details>
<summary>
関数func_greeting内に関数print_greeting（nameを受け取り挨拶を表示する）を定義して関数print_greetingを返す
</summary>

```python
def func_greeting(name):
    def print_greeting():
        print(f'こんにちは。{name}さん')
    return print_greeting

func = func_greeting('john')
```
</details>

<details>
<summary>
nameを受け取り挨拶を表示する関数greetingsと、funcと名前を受け取りfuncの実行と挨拶の続きを表示する関数after_greetingを実行
</summary>

```python
def after_greeting(func, name):
    func(name)
    print(f'きょうはいいお天気ですね')

def greeting(name):
    print(f'こんにちは。{name}さん')

after_greeting(greeting, 'john')
'''
こんにちは。johnさん
今日はいいお天気ですね
'''
```
</details>

<details>
<summary>
実行された関数名を表示するラッパー関数wrap_functionを返すデコレーター関数my_decoratorと、挨拶を表示する関数greetingを作成
</summary>

```python
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
```
</details>

<details>
<summary>
上記をデコレーター化
</summary>

```python
def my_decorator(func):
    def wrap_function():
        func()
        print(f'function: {func.__name__} called')
    return wrap_function

@my_decorator
def greeting():
    print('こんにちは')

greeting()
```
</details>

### 3.7.3 functools.wrapsを使用する

### 3.7.4 デコレーター：よくある使い方