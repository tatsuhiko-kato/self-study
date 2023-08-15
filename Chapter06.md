# self-study
# 6 テキストの処理
## 6.1 一般的な文字列操作を行う - str, string
### 6.1.1 文字列リテラルの書き方
### 6.1.2 文字列以外のオブジェクトを文字列に変換する
### 6.1.3 文字列のチェックメソッド
文字列のチェックメソッド

```python
'123abc'  # 文字列が数字と文字のみ
'abcd'  # 文字列が文字のみ（日本語などの非ASCII含む）
'UPPERCASE'  # 文字列が全て大文字
'losercase'  # 文字列が全て小文字
'Title String'  # 先頭のみ大文字であとは小文字
num1 = '123456789'
num2 = '１２３４５６７８９'
num3 = '①②③'
num4 = 'Ⅳ'
num5 = '一億二千三百四十五万'
num.isdecimal(), num.isdigit(), num.isnumeric()
```
<details>
<summary>
文字列のチェックメソッド
</summary>

```python
'123abc'.isalnum()  # 文字列が数字と文字のみ
'abcd'.isalpha()  # 文字列が文字のみ（日本語などの非ASCII含む）
'UPPERCASE'.isupper()  # 文字列が全て大文字
'losercase'.islower()  # 文字列が全て小文字
'Title String'.istitle  # 先頭のみ大文字であとは小文字
num1.isdecimal(), num1.isdigit(), num1.isnumeric()
'''
(True, True, True)
'''
num2.isdecimal(), num2.isdigit(), num2.isnumeric()
'''
(True, True, True)
'''
num3.isdecimal(), num3.isdigit(), num3.isnumeric()
'''
(False, True, True)
'''
num4.isdecimal(), num4.isdigit(), num4.isnumeric()
'''
(False, False, True)
'''
num5.isdecimal(), num5.isdigit(), num5.isnumeric()
'''
(False, False, True)
'''
```
</details>

### 6.1.4 文字列の変換

```python
text = 'HELLO world!'
# 全て大文字に変換
# 全て小文字に変換
# 大文字を小文字に、小文字を大文字に変換
# 先頭１文字を大文字に、それ以外を小文字に変換
# 単語ごとに大文字１文字＋小文字の形式に変換
# 'world'を'python'に変換
# １つ目のLのみlに変換
word = 'aaa_bbb_ccc'
# 先頭および末尾から「a」「c」を除去
# 先頭の「a」を除去
# 末尾の「c」を除去
# 先頭の「aaa_除去
# 末尾の「_ccc」を除去
number = 12'
# ５桁になるように左をゼロ埋め

```

<details>
<summary>
文字列の変換メソッドの使用例
</summary>

```python
text.upper()
text.lower()
text.swapcase()
text.title()
text.replace('world', 'python')
text.replace('L', 'l', 1)
word.strip('ac')
word.lstrip('a')
word.rstrip('c')
word.removeprefix('aaa_')
word.removesuffix('_ccc')
number.zfill(5)
```
</details>

### 6.1.5 その他の文字列メソッド
### 6.1.6 文字列定数を利用する

## 6.2 フォーマットと文字列リテラル
### 6.2.1 f-stringの書き方
### 6.2.2 =を付けた出力
### 6.2.3 フォーマットの指定方法
### 6.2.4 f-string導入前の文字列フォーマット方法

## 6.3 正規表現を扱う - re
### 6.3.1 基本的な関数

```python
import re
re.search('a.c', 'abcde')
re.match('a.c', 'abcde')
re.search('.c', 'abcde')
re.match('.c', 'abcde')
```

<details>
<summary>
基本的な正規表現のマッチング処理
</summary>

```python
'''
<re.Match object; span=(0, 3), match='abc'>
<re.Match object; span=(0, 3), match='abc'>
<re.Match object; span=(1, 3), match='bc'>
Noneを返す
'''
```
</details>

### 6.3.2 reモジュールの定数（フラグ）
### 6.3.3 正規表現オブジェクト

<details>
<summary>
関数と正規表現オブジェクト
</summary>

```python
import re
pattern = re.compile('a.c')
pattern.search('abcde')
pattern.match('abcde')
```
</details>

### 6.3.4 マッチオブジェクト
### 6.3.5 re: よくある使い方
### 6.3.6 re：ちょっと役立つ周辺知識
### 6.3.7 re：よくあるエラーと対処法

## 6.4 Unicodeデータベースへアクセスする - unicodedata
### 6.4.1 Unicode文字と文字の名前を変換する
### 6.4.2 Unicode文字列の正規化
### 6.4.3 unicodedata：よくある使い方
### 6.4.4 unicodedata：ちょっと役立つ周辺知識
