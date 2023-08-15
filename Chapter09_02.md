# self-study
# 9 データ型とアルゴリズム
## 9.2 さまざまなコンテナー型を扱う - collections
### 9.2.1 データの件数をカウントする - Counter

```python
from collections import Counter
c = Counter('supercalifragilisticexpialidocious')
# cの中身を出力する

import random
li = ['spam'] * 100 + ['ham'] * 90 + ['egg'] * 110
random.shuffle(li)
# liの長さを出力する
```

<details>
<summary>
Counterオブジェクトを生成する
</summary>

```python
>>> from collections import Counter
>>> c = Counter('supercalifragilisticexpialidocious')

# cの中身を出力する
>>> c
Counter({'i': 7, 's': 3, 'c': 3, 'a': 3, 'l': 3, 'u': 2, 'p': 2, 'e': 2, 'r': 2, 'o': 2, 'f': 1, 'g': 1, 't': 1, 'x': 1, 'd': 1})

>>> import random
>>> li = ['spam'] * 100 + ['ham'] * 90 + ['egg'] * 110
>>> random.shuffle(li)# liの長さを出力する
>>> Counter(li)
Counter({'egg': 110, 'spam': 100, 'ham': 90})
```
</details>

```python
from collections import Counter
c = Counter(a=4, b=1, c=-2, d=2)
# カウンターの数分キーを返す
```

<details>
<summary>
Counterオブジェクトのメソッドの利用例
</summary>

```python
>>> from collections import Counter
>>> c = Counter(a=4, b=1, c=-2, d=2)
>>> c
Counter({'a': 4, 'd': 2, 'b': 1, 'c': -2})

# カウンターの数分キーを返す
>>> list(c.elements())
['a', 'a', 'a', 'a', 'b', 'd', 'd']

```
</details>

### 9.2.2 デフォルト値を持った辞書 - defaultdict
### 9.2.3 データの挿入順を維持する辞書 - OrderedDict
### 9.2.4 名前付きフィールドを持つタプル - namedtuple
### 9.2.5 collections：よくある使い方

```python
from collections import defaultdict
# デフォルト値が0のdefaultdict 'dd1'を作成し、キーが'spam'の値を出力
# デフォルト値が空のリストのdefaultdict 'dd2'を作成し、キーが'spam'の値を出力
```

<details>
<summary>
defaultdictを使用する例
</summary>

```python
>>> from collections import defaultdict

# デフォルト値が0のdefaultdict 'dd1'を作成し、キーが'spam'の値を出力
>>> dd1 = defaultdict(int)
>>> dd1['spam']
0

# デフォルト値が空のリストのdefaultdict 'dd2'を作成し、キーが'spam'の値を出力
>>> dd2 = defaultdict(list)
>>> dd2['spam']
[]
```
</details>