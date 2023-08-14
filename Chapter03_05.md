# self-study
# 3 Pythonの言語仕様
## 3.5 内包表記、ジェネレーター式
### 3.5.1 リスト内包表記

```python
number_list = []
for i in range(10):
    number_list.append(i**2)
'''
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
'''
```

<details>
<summary>
リスト内包表記を使用してnumber_listを作成
</summary>

```python
number_list = [i**2 for i in range(10)]
number_list
'''
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
'''
```
</details>

<details>
<summary>
偶数のみをリストに追加
</summary>

```python
number_list = [i**2 for i in range(10) if i % 2 == 0]
number_list
'''
[0, 4, 16, 36, 64]
'''
```
</details>

### 3.5.3 内包表記、ジェネレータ式：よくある使い方

```python
arr = [1.4, 2.0, 3.5, 2.25, 1.98]
```

<details>
<summary>
arrの中身を1つずつround関数で丸めたものをリストにする
</summary>

```python
list(map(round, arr))
'''
[1, 2, 4, 2, 2]
'''
[round(n) for n in arr]
'''
[1, 2, 4, 2, 2]
'''
```
</details>

<details>
<summary>
arrの中身を2以上でフィルターしたものをround関数で丸めリストにする
</summary>

```python
list(map(round, filter(lambda n: n>2, arr)))
'''
[4, 2]
'''
[round(n) for n in arr if n > 2]
'''
[4, 2]
'''
```
</details>