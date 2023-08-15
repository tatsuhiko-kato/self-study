# self-study
# 9 データ型とアルゴリズム
## 9.1 ソート - sorted, sort, oprator
### 9.1.1 sorted()関数

```python
seq = [0, 4, 1, 2, 3, 5]
# ソート結果を出力
# 降順ソート結果を出力
# 基のリストを出力
```

<details>
<summary>
ソートの基本
</summary>

```python
# ソート結果を出力
>>> seq = [0,4,1,2,3,5]

>>> sorted(seq)
[0, 1, 2, 3, 4, 5]

# 降順ソート結果を出力
>>> sorted(seq, reverse=True)
[5, 4, 3, 2, 1, 0]

# 基のリストを出力
>>> seq
[0, 4, 1, 2, 3, 5]
```

</details>

```python
seq_str = ['spam', 'ham', 'egg']
# 文字列のソート結果を出力
```

<details>
<summary>
リストの要素が文字列の場合
</summary>

```python
seq_str = ['spam', 'ham', 'egg']
# 文字列のソート結果を出力
>>> sorted(seq_str)
['egg', 'ham', 'spam']
```
</details>

### 9.1.2 reversed()関数

```python
seq = [0,4,1,2,3,5]
# 逆順シーケンスをrev_seqに格納
```

<details>
<summary>
逆順シーケンスの取得
</summary>

```python
>>> seq = [0,4,1,2,3,5]
# 逆順シーケンスをrev_seqに格納
>>> rev_seq = reversed(seq)
>>> for element in rev_seq:
...     print(element)
... 
5
3
2
1
4
0
```
</details>

### 9.1.3 リストのsort(), reverse()メソッド

```python
seq1 = [0,4,1,2,3,5]
# seq1のソートを実行し、seq1を出力
seq2 = [0,4,1,2,3,5]
# seq2の降順ソートを実行し、seq2を出力
seq3 = [0,4,1,2,3,5]
# seq3を逆順に変更し、seq3を出力
```

<details>
<summary>
リストのソートと逆順への変換処理
</summary>

```python
>>> seq1 = [0,4,1,2,3,5]
# seq1のソートを実行し、seq1を出力
>>> seq1.sort()
>>> seq1
[0, 1, 2, 3, 4, 5]

# seq2の降順ソートを実行し、seq2を出力
>>> seq2.sort(reverse=True)
>>> seq2
[5, 4, 3, 2, 1, 0]

# seq3を逆順に変更し、seq3を出力
>>> seq3.reverse()
>>> seq3
[5, 3, 2, 1, 4, 0]
>>> 
```
</details>

### 9.1.4 key引数

```python
seq_str = ['B','D','a', 'c']
# keyを指定せずにソートした結果を出力
# 小文字に変換してソートした結果を出力
```

<details>
<summary>
リストが文字列の場合のソート
</summary>

```python
seq_str = ['B','D','a', 'c']
# keyを指定せずにソートした結果を出力
>>> sorted(seq_str)
['B', 'D', 'a', 'c']

# 小文字に変換してソートした結果を出力
>>> sorted(seq_str, key=str.lower)
['a', 'B', 'c', 'D']

```

</details>

### 9.1.5 operatorモジュール

```python
from operator import itemgetter
data = [(1,40,200), (3, 10, 100), (2, 20, 300), (1, 30, 300)]
# keyを指定せずにソートした結果を出力
# インデックス2でソートし、それ以外はもとの順番を保った結果を出力
# インデックス2でソートし、同じ場合はインデックス0でソートした結果を出力
```

<details>
<summary>
タプルの要素をソート
</summary>

```python
>>> from operator import itemgetter
>>> data = [(1,40,200), (3, 10, 100), (2, 20, 300), (1, 30, 300)]

# keyを指定せずにソートした結果を出力
>>> sorted(data)
[(1, 30, 300), (1, 40, 200), (2, 20, 300), (3, 10, 100)]

# インデックス2でソートし、それ以外はもとの順番を保った結果を出力
>>> sorted(data, key=itemgetter(2))
[(3, 10, 100), (1, 40, 200), (2, 20, 300), (1, 30, 300)]

# インデックス2でソートし、同じ場合はインデックス0でソートした結果を出力
>>> sorted(data, key=itemgetter(2, 0))
[(3, 10, 100), (1, 40, 200), (1, 30, 300), (2, 20, 300)]
```
</details>

```python
from operator import attrgetter
from datetime import date
dates = [date(1989, 1, 4), date(1970, 11, 28), date(1984, 3, 4)]
# monthでソートし、次にdayでソート
```

<details>
<summary>
クラス属性を指定したソート
</summary>

```python
from operator import attrgetter
from datetime import date
dates = [date(1989, 1, 4), date(1970, 11, 28), date(1984, 3, 4)]

# monthでソートし、次にdayでソート
>>> sorted(dates, key=attrgetter("month", "day"))
[datetime.date(1989, 1, 4), datetime.date(1984, 3, 4), datetime.date(1970, 11, 28)]

```
</details>

### 9.1.6 ソート：ちょっと役立つ周辺知識
### 9.1.7 sorted, sort, operator：よくあるエラーと対処法
