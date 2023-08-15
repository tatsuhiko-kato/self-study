# self-study
# 5 型ヒント
## 5.1 型ヒント
### 5.1.1 型ヒントとは
### 5.1.2 基本的な型ヒントの一覧と書き方

```python
def say_hello(name):
    return f"Hello, {name}"

name = 'TypeHinto-kun'
```
<details>
<summary>
型ヒントを利用
</summary>

```python
def say_hello(name: str) -> str:
    return f"Hello, {name}"

name: str = 'TypeHinto-kun'
message = sey_hello(name)
```
</details>

コンテナーの型付け
```python
hobby = ['ゲーム', 'マンガ']
favorate = {'sduty': 'プログラミング', 'movie': 'モンティパイソン'}
like_num = {1, 3, 5}
food = ('バナナ', 'ハンバーグ')
```
<details>
<summary>
コンテナーの型付け
</summary>

```python
hobby: list = ['ゲーム', 'マンガ']
favorate: dict = {'sduty': 'プログラミング', 'movie': 'モンティパイソン'}
like_num: set = {1, 3, 5}
food: tuple = ('バナナ', 'ハンバーグ')
```
</details>

<details>
<summary>
コンテナー内の要素の型付け
</summary>

```python
hobby: list[str] = ['ゲーム', 'マンガ']
favorate: dict[str, str] = {'sduty': 'プログラミング', 'movie': 'モンティパイソン'}
like_num[int]: set = {1, 3, 5}
food: tuple[str, str] = ('バナナ', 'ハンバーグ')
```

### 5.1.3 typingモジュールを利用した型ヒント
### 5.1.4 型ヒント：よくある使い方