# self-study
# 9 データ型とアルゴリズム
## 9.6 イテレータの組み合わせで処理を組み立てる - itertools
### 9.6.1 イテラブルオブジェクトを連結する

```python
import itertools
# リスト['A', 'B'], 文字列'ab'、range(3)を連結しitに格納
# itの要素を１つづつ出力
```

<details>
<summary>
サンプルコード
</summary>

```python
>>> import itertools

# リスト['A', 'B'], 文字列'ab'、range(3)を連結しitに格納
>>> it = chain(['A', 'B'], 'ab', range(3))

# itの要素を１つづつ出力
>>> for element in it:
...     element
... 
'A'
'B'
'a'
'b'
0
1
2
```
</details>

```python
import itertools
text = 'aaabbcdddaabb'
# textをソートしてsorterd_textに格納
# sorted_textをgroup化してgrouped_textに格納
# grouped_textをグループ単位で出力
```

<details>
<summary>
サンプルコード
</summary>

```python
>>> import itertools
>>> text = 'aaabbcdddaabb'

# textをソートしてsorterd_textに格納
>>> sorted_text = ''.join(sorted(text))
>>> sorted_text
'aaaaabbbbcddd'

# sorted_textをgroup化してgrouped_textに格納
>>> grouped_text = itertools.groupby(sorted_text)

# grouped_textをグループ単位で出力
>>> for key, value in grouped_text:
...     print(f'{key}: {list(value)}')
... 
a: ['a', 'a', 'a', 'a', 'a']
b: ['b', 'b', 'b', 'b']
c: ['c']
d: ['d', 'd', 'd']
```
</details>

### 9.6.3 イテレータから範囲を指定して値を取得する

```python
import itertools
li = list(range(10))
# リストの最初の5要素をislicオブジェクトislice_objectに格納し、リストに変換して出力
```

<details>
<summary>
サンプルコード
</summary>

```python
>>> import itertools
>>> li = list(range(10))

# リストの最初の5要素をislicオブジェクトislice_objectに格納し、リストに変換して出力
>>> islice_object = itertools.islice(li, 5)
>>> list(islice_object)
[0, 1, 2, 3, 4]
```
</details>

### 9.6.4 複数のイテラブルオブジェクトの要素からタプルを作成する

```python
it1 = (1,2,3)
it2 = ['abc', 'ABC', '123']
it3 = 'あいう'
# 3つのイテラブルオブジェクトから１つずつ取り出して出力する
```

<details>
<summary>
サンプルコード
</summary>

```python
>>> it1 = (1,2,3)
>>> it2 = ['abc', 'ABC', '123']
>>> it3 = 'あいう'

# 3つのイテラブルオブジェクトから１つずつ取り出して出力する
>>> for v in zip(it1, it2, it3):
...     print(v)
... 
(1, 'abc', 'あ')
(2, 'ABC', 'い')
(3, '123', 'う')
```
</details>

```python
import itertools
it1 = 'abcde'
it2 = '123'
it3 = 'あいうえ'
# 3つのイテラブルオブジェクトから１つずつ取り出し、要素がない場合は'-'で埋めて出力する
```

<details>
<summary>
サンプルコード
</summary>

```python
>>> import itertools
>>> it1 = 'abcde'
>>> it2 = '123'
>>> it3 = 'あいうえ'

# 3つのイテラブルオブジェクトから１つずつ取り出し、要素がない場合は'-'で埋めて出力する
>>> for v in itertools.zip_longest(it1, it2, it3, fillvalue='-'):
...     print(v)
... 
('a', '1', 'あ')
('b', '2', 'い')
('c', '3', 'う')
('d', '-', 'え')
('e', '-', '-')
```
</details>

### 9.6.5 データを組み合わせたイテレータを取得する

```python
import itertools
it1 = 'ABC'
it2 = 'ABC'
# it1とit2のデカルト積を出力
# it1のうちの２つの順列を出力
# 重複なしの組み合わせを出力
# 重複ありの組み合わせを出力
```

<details>
<summary>
サンプルコード
</summary>

```python
>>> import itertools
>>> it1 = 'ABC'
>>> it2 = 'ABC'

# it1とit2のデカルト積を出力
>>> list(itertools.product(it1, it2))
[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]

# it1のうちの２つの順列を出力
>>> list(itertools.permutations(it1, 2))
[('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

# 重複なしの組み合わせを出力
>>> list(itertools.combinations(it1, 2))
[('A', 'B'), ('A', 'C'), ('B', 'C')]

# 重複ありの組み合わせを出力
>>> list(itertools.combinations_with_replacement(it1, 2))
[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
```
</details>

### 9.6.6 itertools：よくある使い方
### 9.6.7 itertools：ちょっと役立つ周辺知識
