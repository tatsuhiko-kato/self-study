# self-study
# 2 コーディング規則
## 2.1 Python標準のスタイルガイド - PEP8
### 2.1.1 PEP8で定義されているルール
### 2.1.2 コードのレイアウト
<details>
<summary>
インデント
</summary>

```python
# 丸カッコの先頭に揃えるパターン  
# 先頭の値を縦で揃え、定義の始めの位置に閉じカッコを揃えるパターン
</details>


<details>
<summary>
空行
</summary>

```python
# トップレベルの関数やクラスの間は２行空ける  
# クラス内部のメソッドは１行空ける  
```
</details>

<details>
<summary>
import
</summary>

```python
異なるモジュールはimport文を分ける
同じモジュールはimport文をまとめる
サードバーティのモジュールは標準ライブラリのあとにimportする
ローカルのモジュールは最後にimportする
```
</details>

<details>
<summary>
空白文字
</summary>

```python
余計な空白文字を使わない
代入演算子や比較演算子などの両側には１つだけ空白文字を入れる
カンマの後ろに空白文字を入れる
閉じカッコなど終わりを表す文字の前には空白文字を入れない
```
</details>

### 2.1.3 コメント
<details>
<summary>
ブロックコメント
</summary>

```python
# コードと同じインデントで各  
# コメント自体は、１つの#と１つの空白の後ろに書く  
```
</details>

<details>
<summary>
インラインコメント
</summary>
コードとコメントの間は２つ以上のスペースを書く
コメント自体は、１つの#と１つのスペースの後ろに書く
</div></details>

<details>
<summary>
docstring
</summary>

```python
# 関数やメソッドの説明はdefの直後に書く
# """で始まり、"""で終わる行とする
# 説明が複数行の場合は、１行目のあとに空行を書く
```
</details>

### 2.1.4 命名規則
<details>
<summary>
パッケージとモジュールの名前
</summary>

```python
# lowercase
```
</details>

<details>
<summary>
クラスの名前
</summary>

```python
CamelCase
```
</details>

<details>
<summary>
関数や変数の名前
</summary>

```python
lowercase または lower_case_with_underscores
```
</details>

<details>
<summary>
定数
</summary>

```python
UPPERCASE または UPPER_CASE_WITH_UNDERSCORES
```
</details>

<details>
<summary>
例外の名前
</summary>

```python
UPPERCASE または UPPER_CASE_WITH_UNDERSCORES
```
</details>
