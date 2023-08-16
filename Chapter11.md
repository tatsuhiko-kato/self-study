# self-study
# 11 ファイルとディレクトリへのアクセス
## 11.1 ファイルパス操作を直感的に行う
### 11.1.1 クラス構成
### 11.1.2 純粋パスを扱う

```python
from pathlib import PurePath, Path
# PurePathオブジェクト'spam.txt'を生成
# 'spam', 'ham', 'eggs.txt'を連結してPurePathオブジェクトを生成
# '/user'をPathオブジェクトpに格納し、'/user/bin/python3'を出力
```

<details><summary>sample code</summary>

```python
>>> from pathlib import PurePath, Path

# PurePathオブジェクト'spam.txt'を生成
>>> PurePath('spam.txt')
PurePosixPath('spam.txt')

# 'spam', 'ham', 'eggs.txt'を連結してPurePathオブジェクトを生成
>>> PurePath('spam', 'ham', 'eggs.txt')
PurePosixPath('spam/ham/eggs.txt')

# '/user'をPathオブジェクトpに格納し、'/user/bin/python3'を出力
>>> p / 'bin' / 'python3'
PosixPath('/user/bin/python3')
```

</details>

```python
from pathlib import PurePath, PureWindowsPath
p = PurePath('spam/ham/egg.tar.gz')
wp = PureWindowsPath('c:/Program Files/spam/ham.exe')
# p, wpの各要素を取得
# p, wpのドライブを取得
# p, wpのルートを取得
# wpのドライブとルートを結合した文字列を取得
# pの上位のパスのシーケンスを出力
# pの直接の上位のパスを取得
# pの末尾の要素を取得
# pの拡張子を取得
# pの拡張子のリストを取得
# pの末尾の要素から拡張子を除いたものを取得
```

<details><summary>sample code</summary>

```python
>>> from pathlib import PurePath, PureWindowsPath
>>> p = PurePath('spam/ham/egg.tar.gz')
>>> wp = PureWindowsPath('c:/Program Files/spam/ham.exe')

# p, wpの各要素を取得
>>> p.parts
('spam', 'ham', 'egg.tar.gz')
>>> wp.parts
('c:\\', 'Program Files', 'spam', 'ham.exe')

# p, wpのドライブを取得
>>> p.drive
''
>>> wp.drive
'c:'

# p, wpのルートを取得
>>> p.root
''
>>> wp.root
'\\'

# wpのドライブとルートを結合した文字列を取得
>>> p.anchor
''
>>> wp.anchor
'c:\\'

# pの上位のパスのシーケンスを出力
>>> for parent in p.parents:
...     parent
... 
PurePosixPath('spam/ham')
PurePosixPath('spam')
PurePosixPath('.')

# pの直接の上位のパスを取得
>>> p.parent
PurePosixPath('spam/ham')

# pの末尾の要素を取得
>>> p.name
'egg.tar.gz'

# pの拡張子を取得
>>> p.suffix
'.gz'

# pの拡張子のリストを取得
>>> p.suffixes
['.tar', '.gz']

# pの末尾の要素から拡張子を除いたものを取得
>>> p.stem
'egg.tar'
```

</details>

```python
from pathlib import PurePath
p1 = PurePath('/spam/ham/eggs.txt')
p2 = PurePath('eggs.txt')
# p1, p2が絶対パスか判定
# p1が'/spam'に対して相対か判定
# p1が'/ham'に対して相対か判定
# p1がパターン'*.txt'に一致するか判定
# p1のnameを'hoge.txt'に変更
# p1のstemを'fuga'に変更
# p1の拡張子を'.py'に変更
# p1の拡張子を削除
```

<details><summary>sample code</summary>

```python
>>> from pathlib import PurePath
>>> p1 = PurePath('/spam/ham/eggs.txt')
>>> p2 = PurePath('eggs.txt')

# p1, p2が絶対パスか判定
>>> p1.is_absolute()
True
>>> p2.is_absolute()
False

# p1が'/spam'に対して相対か判定
>>> p1.is_relative_to('/spam')
True

# p1が'/ham'に対して相対か判定
>>> p1.is_relative_to('/ham')
False

# p1がパターン'*.txt'に一致するか判定
>>> p1.match('*.txt')
True

# p1のnameを'hoge.txt'に変更
>>> p1.with_name('hoge.txt')
PurePosixPath('/spam/ham/hoge.txt')

# p1のstemを'fuga'に変更
>>> p1.with_stem('fuga')
PurePosixPath('/spam/ham/fuga.txt')

# p1の拡張子を'.py'に変更
>>> p1.with_suffix('.py')
PurePosixPath('/spam/ham/eggs.py')

# p1の拡張子を削除
>>> p1.with_suffix('')
PurePosixPath('/spam/ham/eggs')

```

</details>

### 11.1.3 具象パスを扱う

```python
from pathlib import Path
# 現在のディレクトリを取得
# ホームディレクトリを取得
p = Path('python.txt')
# pがあるかどうか判定
# pがファイルかどうか判定
# pを開いて中身を読み込む
# pを削除し、pがあるかどうか判定
# pを作成し、pに'Python!'を書き込む
# pの絶対パスを取得

```

<details><summary>sample code</summary>

```python
>>> from pathlib import Path
# 現在のディレクトリを取得
>>> Path.cwd()
PosixPath('/workspaces/self-study')

# ホームディレクトリを取得
>>> Path.home()
PosixPath('/home/codespace')

# pがあるかどうか判定
>>> p = Path('python.txt')
>>> p.exists()

# pがファイルかどうか判定
>>> p.is_file()
True

# pを開いて中身を読み込む
>>> with p.open(encoding='utf-8') as f:
...     f.read()
... 
'Python!'

# pを削除し、pがあるかどうか判定
>>> p.unlink()
>>> p.exists()
False

# pを作成し、pに'Python!'を書き込む
>>> p.touch()
>>> p.write_text('Python!', encoding='utf-8')
7

# pの絶対パスを取得
>>> p.resolve()
PosixPath('/workspaces/self-study/python.txt')
```

</details>

### 11.1.4 pathlib：よくある使い方
### 11.1.5 pathlib：ちょっと役立つ周辺知識
### 11.1.6 pathlib：よくあるエラーと対処法

## 11.2 一時的なファイルやディレクトリを生成する
### 11.2.1 一時ファイルを作成する

```python
import tempfile
# tempfileを作成し、tmpfに格納
# tmpfにb'test test tst\n'を書き込む
# オフセット0に移動
# 読み込み
```

<details>
<summary>サンプルコード</summary>

```python
>>> import tempfile
# tempfileを作成し、tmpfに格納
# tmpfにb'test test tst\n'を書き込む
# オフセット0に移動
# 読み込み
>>> import tempfile
>>> with tempfile.TemporaryFile() as tmpf:
...     tmpf.write(b'test test test\n')
...     tmpf.seek(0)
...     tmpf.read()
... 
15
0
b'test test test\n'
```
</details>

### 11.2.2 一時ディレクトリを作成する

```python
import tempfile
from pathlib import Path
# ディレクトリtmpdirnameを作成
# ディレクトリ名を出力
# ディレクトリの存在を確認
# ディレクトリの下にファイルを作成
# ファイルの存在を確認
```

<details>
<summary>サンプルコード</summary>

```python
>>> import tempfile
>>> from pathlib import Path

# ディレクトリtmpdirnameを作成
# ディレクトリ名を出力
# ディレクトリの存在を確認
# ディレクトリの下にファイルを作成
# ファイルの存在を確認
>>> with tempfile.TemporaryDirectory() as tmpdir:
...     tmpdir
...     p = Path(tmpdir)
...     p.exists()
...     p2 = p / 'hoge.txt'
...     p2.touch()
...     p2.exists()
... 
'/tmp/tmp6fstc01k'
True
True
```
</details>

## 11.3 高レベルなファイル操作を行う
### 11.3.1 ファイルをコピーする

```python
import shutil
# ファイル11_03_01_a.txtをファイル11_03_01_b.txtにコピー
# ファイル11_03_01_a.txtをファイル11_03_01_b.txtにコピーし、パーミッションもコピー
# ファイル11_03_01_a.txtをファイル11_03_01_b.txtにコピーし、全てのメタデータを保持
# ファイルのリストを出力（PowerShell)
```

<details><summary>sample code</summary>

```python
>>> import shutil

# ファイル11_03_01_a.txtをファイル11_03_01_b.txtにコピー
>>> shutil.copyfile('11_03_01_a.txt', '11_03_01_b.txt')
'11_03_01_b.txt'

# ファイル11_03_01_a.txtをファイル11_03_01_b.txtにコピーし、パーミッションもコピー
>>> shutil.copy('11_03_01_a.txt', '11_03_01_c.txt')
'11_03_01_c.txt'

# ファイル11_03_01_a.txtをファイル11_03_01_b.txtにコピーし、全てのメタデータを保持
>>> shutil.copy2('11_03_01_a.txt', '11_03_01_d.txt')
'11_03_01_d.txt'

# ファイルのリストを出力（PowerShell)
$ ls -l
```

</details>

### 11.3.2 再帰的にディレクトリやファイルを操作する
### 11.3.3 shutil：よくある使い方
### 11.3.4 shutil：ちょっと役立つ周辺知識
