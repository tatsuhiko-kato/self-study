# self-study
# 10 汎用OS・ランタイムサービス
## 10.1 OSの機能を利用する
### 10.1.1 実行中のプロセス属性の操作

```python
import os
# ユーザーのホームディレクトリが格納された環境変数を出力
```

<details>
<summary>サンプルコード</summary>

```python
>>> import os

# ユーザーのホームディレクトリが格納された環境変数を出力
>>> os.environ['HOME']
'/home/codespace'
```
</details>

### 10.1.2 ファイルとディレクトリの操作

```python
import os
# 現在の作業ディレクトリを出力
# /tmpディレクトリに移動
# testディレクトリを作成
# 現在のディレクトリ内のファイルとディレクトリのリストを出力
# testディレクトリを削除
```

<details>
<summary>サンプルコード</summary>

```python
>>> import os

# 現在の作業ディレクトリを出力
>>> os.getcwd()
'/workspaces/self-study'

# /tmpディレクトリに移動
>>> os.chdir('/tmp')

# testディレクトリを作成
>>> os.mkdir('test')

# 現在のディレクトリ内のファイルとディレクトリのリストを出力
>>> os.listdir('.')
['test']

# testディレクトリを削除
>>> os.rmdir('test')
```
</details>

### 10.1.3 さまざまなシステム情報へのアクセス
### 10.1.4 ランダムな文字列の生成

```python
import os
# 10バイトのランダムなbypesオブジェクトを出力
```

<details>
<summary>サンプルコード</summary>

```python
>>> import os
# 10バイトのランダムなbypesオブジェクトを出力
>>> os.urandom(10)
b'\xa7\xfaX\x1f\xd1\xb6\xee\x93\xdb\x14'
```
</details>

### 10.1.5 os：よくある使い方
### 10.1.6 os：ちょっと役立つ周辺知識
### 10.1.7 os：よくあるエラーと対処法

## 10.2 ストリームを扱う
### 10.2.1 インメモリなテキストストリームを扱う

```python
import io
# 初期値"this is test/n"をStringIOオブジェクトstreamに格納
# ストリームから10文字読みだして出力
# 現在のオフセットを出力
# オフセットをストリームの末尾に変更
# ストリームに'test'と書き込み
# ストリームが保持する全ての内容を出力
# ストリームを閉じる
# ブランクのストリームst2をwithブロックで生成し、'test'を書き込む
# the_zen_of_pythonをStringIOオブジェクトst3に格納し、１行ずつ出力
```

<details>
<summary>サンプルコード</summary>

```python
>>> import io

# 初期値"this is test/n"をStringIOオブジェクトst1に格納
>>> st1 = io.StringIO("this is test\n")

# ストリームから10文字読みだして出力
>>> st1.read(10)
'this is te'

# 現在のオフセットを出力
>>> st1.tell()
10

# オフセットをストリームの末尾に変更
>>> st1.seek(0, io.SEEK_END)
13

# ストリームに'test'と書き込み
>>> st1.write('test')
4

# ストリームが保持する全ての内容を出力
>>> print(st1.getvalue())
this is test
test

# ストリームを閉じる
>>> st1.close()

# ブランクのストリームst2をwithブロックで生成し、'test'を書き込む
>>> with io.StringIO() as st2:
...     st2.write('test')
... 
4

# the_zen_of_pythonをStringIOオブジェクトst3に格納し、１行ずつ出力
>>> the_zen_of_python = """
... The Zen of Python, by Tim Peters
... 
... Beautiful is better than ugly.
... Explicit is better than implicit.
... Simple is better than complex.
... Complex is better than complicated.
... Flat is better than nested.
... Sparse is better than dense.
... Readability counts.
... Special cases aren't special enough to break the rules.
... Although practicality beats purity.
... Errors should never pass silently.
... Unless explicitly silenced.
... In the face of ambiguity, refuse the temptation to guess.
... There should be one-- and preferably only one --obvious way to do it.
... Although that way may not be obvious at first unless you're Dutch.
... Now is better than never.
... Although never is often better than *right* now.
... If the implementation is hard to explain, it's a bad idea.
... If the implementation is easy to explain, it may be a good idea.
... Namespaces are one honking great idea -- let's do more of those!
... """
>>> st3 = io.StringIO(the_zen_of_python)
>>> for line in st3:
...     line
... 
'\n'
'The Zen of Python, by Tim Peters\n'
'\n'
'Beautiful is better than ugly.\n'
'Explicit is better than implicit.\n'
'Simple is better than complex.\n'
'Complex is better than complicated.\n'
'Flat is better than nested.\n'
'Sparse is better than dense.\n'
'Readability counts.\n'
"Special cases aren't special enough to break the rules.\n"
'Although practicality beats purity.\n'
'Errors should never pass silently.\n'
'Unless explicitly silenced.\n'
'In the face of ambiguity, refuse the temptation to guess.\n'
'There should be one-- and preferably only one --obvious way to do it.\n'
"Although that way may not be obvious at first unless you're Dutch.\n"
'Now is better than never.\n'
'Although never is often better than *right* now.\n'
"If the implementation is hard to explain, it's a bad idea.\n"
'If the implementation is easy to explain, it may be a good idea.\n'
"Namespaces are one honking great idea -- let's do more of those!\n"
```
</details>

### 10.2.2 インメモリなバイナリストリームを扱う
### 10.2.3 ioモジュールをユニットテストで活用する
### 10.2.4 io：よくある使い方
### 10.2.5 io：ちょっと役立つ周辺知識
### 10.2.6 io：よくあるエラーと対処法

## 10.3 インタープリターに関わる情報を取得、操作する
### 10.3.1 コマンドライン引数を取得する
### 10.3.2 ライブラリのインポートパスを操作する
### 10.3.3 プログラムを終了する
### 10.3.4 コンソールの入出力を扱う
### 10.3.5 breakpoint()実行時のフック関数
### 10.3.6 Pythonのバージョン番号を調べる
### 10.3.7 sys：よくある使い方
### 10.3.8 sys：ちょっと役立つ周辺知識
### 10.3.9 sys：よくあるエラーと対処法

## 10.4 コマンドラインオプション、引数を扱う
### 10.4.1 コマンドラインオプションを扱う
### 10.4.2 argparse：よくある使い方
### 10.4.3 argparse：ちょっと役立つ周辺知識
### 10.4.4 argparse：よくあるエラーと対処法

