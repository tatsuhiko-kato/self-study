# self-study
# 3 Pythonの言語仕様
## 3.6 ジェネレーター
### 3.6.1 ジェネレーター

```python
def multiplier(values):
    ret = []
    for in in values:
        ret.append(2 ** i)
    return ret

values = [0, 1, 2, 3, 4, 5]
ret = multiplier(values)
type(ret)
'''
<class 'list'>
'''
ret
'''
[1, 2, 4, 8, 16, 32]
'''
```

<details>
<summary>
2の乗数を返すジェネレーターmultiplier
</summary>

```python
def multiplier(values):
    for i in value:
        yield 2 ** i

values = [0, 1, 2, 3, 4, 5]
ret = multiplier(values)
type(ret)
'''
<class 'generator'>
'''
for in in ret:
    print(i)
'''
0
1
4
9
16
25
'''
```
</details>

<details>
<summary>
前の値の2乗を返すジェネレーター
</summary>

```python
def multiplier():
    num = 1
    while True:
        yield num
        num *= 2

gen = multiplier()
gen
'''
<generator object multiplier at 0x000001CE574A9580>
'''
next(gen)
'''
1
'''
next(gen)
'''
2
'''
next(gen)
'''
4
'''
next(gen)
'''
8
'''
```
</details>

### 3.6.2 list()関数を使用してリストに変換する
<details>
<summary>
ファイル'generator_sample.txt'に含まれるデータの'関数'列の値を取得
</summary>
</details>

### 3.6.3 大きいファイルの処理にジェネレーターを使用する

### 3.6.4 ジェネレーター：よくある使い方

### 3.6.5 ジェネレーター：ちょっと役立つ周辺知識

### 3.6.6 ジェネレーター；よくあるエラーと対処法