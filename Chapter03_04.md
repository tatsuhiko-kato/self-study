# self-study
# 3 Pythonの言語仕様
## 3.4 アンパック
### 3.4.1 アンパック

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
```
<details>
<summary>
辞書のキーをアンパック
</summary>

```python
key1, key2, key3 = my_dict
print(f'{key1}, {key2}, {key3})
'''
a, b, c
'''
```
</details>

<details>
<summary>
辞書の値をアンパック
</summary>

```python
value1, value2, value3 = my_dict.values()
print(f'{value1}, {value2}, {value3})
'''
1, 2, 3
'''
```
</details>

### 3.4.2 ネストしたタプル、リストのアンパック
### 3.4.3 アスタリスクを使ったアンパック

```python
tp = (0, 1, 2, 3, 4)
```

<details>
<summary>
タプルの要素1をa, 要素2をb、それ以降の要素をcに格納
</summary>

```python
a, b, *c = tb
print(f'{a}, {b}, {c}')
```
</details>

### 3.4.4 関数の引数のアンパック
引数のアンパック（リスト）

```python
def sample_func(param1, param2, param3):
    print(f'{param1}, {param2}, {param3})
```

<details>
<summary>
param1=1, param2=2, param3=3をリストで渡す
</summary>

```python
args = [1, 2, 3]
sample_func(*args)
'''
1, 2, 3
'''
```
</details>

引数のアンパック（辞書）

```python
def display_user(name, age, email):
    print(f'{name}, {age}, {email}')
```

<details>
<summary>
キーワード引数name='john', age=30, email='john@example.com'を辞書で受け取る
</summary>

```python
kwargs = {'name': 'john', 'age': 30, 'email': 'john@example.com'}
'''
john, 30, john@example.com
'''
```
</details>

### 3.4.5 アンパック：よくある使い方
辞書のキーと値を一度に取り出す

```python
country_code = {
    'GBR': '英国',
    'TWN': '台湾',
    'JPN': '日本'
}
```

<details>
<summary>
country_codeと国名を表示
</summary>

```python
for key, value in country_code.items():
    print(f'{key}: {value}')
'''
GRB: 英国
TWN: 台湾
JPN: 日本
'''
```
</details>

リストの要素をインデックス番号付きで取得

```python
colorlist = ['Red', 'Blue', 'Green']
```

<details>
<summary>
インデックス番号を取得
</summary>

```python
for i, color in enumerate(colorlist):
    print(f'{i}番目の色は{color}です)
'''
0番目の色はRedです
1番目の色はBlueです
2番目の色はGreenです
'''
```
</details>