# self-study
# 9 データ型とアルゴリズム
## 9.7 ミュータブルなオブジェクトをコピーする
### 9.7.1 浅いコピーを行う

```python
import copy
values = [[0,1], [2,3], [4,5]]
# 浅いコピーをval_cpに格納し、val_cpに[6,7]を追加後、valuesとvalue_cpを出力
# value_cp[1][0]の値を8に変更し、valuesとvalue_cpを出力
```

<details>
<summary>サンプルコード</summary>

```python
>>> import copy
>>> values = [[0,1],[2,3],[4,5]]

# 浅いコピーをval_cpに格納し、val_cpに[6,7]を追加後、valuesとvalue_cpを出力
>>> val_cp = copy.copy(values)
>>> val_cp.append([6,7])
>>> values
[[0, 1], [2, 3], [4, 5]]
>>> val_cp
[[0, 1], [2, 3], [4, 5], [6, 7]]

# value_cp[1][0]の値を8に変更し、valuesとvalue_cpを出力
>>> val_cp[1][0] = 8
>>> values
[[0, 1], [8, 3], [4, 5]]
>>> val_cp
[[0, 1], [8, 3], [4, 5], [6, 7]]
```
</details>

### 9.7.2 深いコピーを行う

```python
import copy
values = [[0,1], [2,3], [4,5]]
# 深いコピーをval_cpに格納し、value_cp[1][0]の値を8に変更し、valuesとvalue_cpを出力
```

<details>
<summary>サンプルコード</summary>

```python
>>> import copy
>>> values = [[0,1],[2,3],[4,5]]

# 深いコピーをval_cpに格納し、value_cp[1][0]の値を8に変更し、valuesとvalue_cpを出力
>>> val_cp = copy.deepcopy(values)
>>> val_cp[1][0] = 8
>>> values
[[0, 1], [2, 3], [4, 5]]
>>> val_cp
[[0, 1], [8, 3], [4, 5]]
```
</details>

### 9.7.3 copy：よくある使い方
### 9.7.4 copy：ちょっと役立つ周辺知識
