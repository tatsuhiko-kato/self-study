# self-study
# 3 Pythonの言語仕様
## 3.3 関数の引数
### 3.3.1 位置引数
<details>
<summary>
位置引数のサンプルコード ※param1='spam', param2='ham', param3='egg'
</summary>

```python
def sample_func(param1, param2, param2):
    print(f'{param1}, {param2}, {param3}')

sample_func('spam', 'ham', 'egg')
'''
spam, ham, egg
'''
```
</details>

### 3.2.2 キーワード引数
<details>
<summary>
キーワード引数のサンプルコード ※param3=3, param2=2, param1=1
</summary>

```python
def sample_func(param1, param2, param2):
    print(f'{param1}, {param2}, {param3}')

sample_func(param3=3, param2=2, param1=1')
'''
1, 2, 3
'''
```
</details>

### 3.3.3 位置引数とキーワード引数の混在
<details>
<summary>
位置引数とキーワード引数のサンプルコード
</summary>

```python
# 位置引数を先にに置き、キーワード引数はそのあとで指定する必要がある
sample_func(1, param3=3, param2=2)
'''
1, 2, 3
'''
sample_func(param3=3, 1, 2)
'''
  File "<stdin>", line 1
    sample_func(param3=3, 1, 2)
'''
sample_func(1, 2, param1=1)
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
'''
```
</details>

### 3.3.4 デフォルト値付き引数
<details>
<summary>
デフォルト値はイミュータブルなオブジェクトを指定
</summary>

```python
# 文字列
# 数値
# タプル
```
</details>

### 3.3.5 可変長位置引数
<details>
<summary>
可変長位置引数のサンプルコード ※1.リストで渡された値を合計して返す関数func_sum, ※2.リストやタプルの要素を可変長引数として渡す場合
</summary>

```python
def func_sum(*args):
    total = 0
    for num in args:
        total += num
    return(total)
func_sum(1,2,3,4,5)
'''
#1
15
'''
num = [1,2,3,4,5]
func_sum(*num)
'''
#2
15
'''
```
</details>

<details>
<summary>
可変長位置引数の定義位置 ※注意点
</summary>

```python
def sample_func(param1, param2, *args)
    print(f'{param1=}')
    print(f'{param2=}')
    print(f'{param3=}')

sample_func(1,2,3,4,5)
'''
param1=1
param2=2
args=(3, 4, 5)
'''
```
</details>

# 3.3.6 可変長キーワード引数
<details>
<summary>
可変長キーワード引数のサンプルコード ※位置引数name='john', 可変長キーワード引数age=30, email='john@example.com'を受け取り、表示する関数sample_func
</summary>

```python
def sample_func(name, **kwargs):
    print(f'{name=}')
    for key, value in kwargs.items():
        print(f'{key}: {value})

sample_func('john', age=30, email='john@example.com')
'''
name='john'
age: 30
email: john@example.com
'''
```
</details>

### 3.3.7 キーワード専用引数
<details>
<summary>
キーワード専用引数のサンプルコード ※位置引数param1=1, キーワード専用引数keyword1=Falseを受け取って表示する関数sample_func
</summary>

```python
def sample_func(param1, *, keyword1):
    print(f'{param1}, {keyword1})

sample_func(1, keyword1=False)
'''
1, False
'''
```
</details>

### 3.3.8 位置専用引数
<details>
<summary>
位置専用引数x=1, y=2を受け取り、合計値を返す関数add
</summary>

```python
def add(x, y, /):
    return x + y

add(1, 2)
'''
3
'''
```
</details>

### 3.3.9 関数の引数：よくある使い方
<details>
<summary>
既に利用されている関数addに引数cを追加
</summary>

```python
def add(a, b, c=0):
    return a + b + c

add(1, 2)
'''
3
'''
add(1, 2, 3)
'''
6
'''
```
</details>

### 3.3.10 関数の引数：よくあるエラーと対処法
```python
def sample_func(a, b, c=[]):
    c.append(a + b)
    return c
sample_func(1, 2)
sample_func(3, 4)
sample_func(5, 6)
```
<details>
<summary>
デフォルト値付きの引数のよくあるエラー
</summary>

```python
'''
[3]
[3, 7]
[3, 7, 11]
```
</details>

<details>
<summary>
正しい例
</summary>

```python
def sample_func(a, b, c=None):
    if c is None:
        c = []
    c.append(a+b)

sample_func(1, 2)
'''
[3]
'''
sample_func(3, 4)
'''
[7]
'''
sample_func(5, 6)
'''
[11]
'''
```
</details>

