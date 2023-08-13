# self-study
# 3 Pythonの言語仕様
## 3.1 例外処理
### 3.1.1 例外を処理する
<details><summary>
例外を発生させる 
※ゼロで割る
</summary><div>
num = 0 / 10
</div></details>

<details><summary>
try-except 
</summary><div>
try:
    num = 10 / 0
    print(f'除算の結果は{num}になります')
except ZeroDivisionError:
    print('0で割ることはできません')
</div></details>

<details><summary>
複数の例外を補足する 
※ZeroDivisionError, TypeError
</summary><div>
try:
    num = 10 / '2'
    print(f'除算の結果は{num}になります')
except ZeroDivisionError:
    print('0で割ることはできません')
except TypeError:
    print('文字列で割ることはできません')
</div></details>

<details><summary>
複数の例外を補足する 
※ZeroDivisionError, TypeError, NameError内容を一時変数で受け取ってexcept節のなかで利用
</summary><div>
try:
    num = 10 / 0
except (ZeroDivisionError, TypeError, NameError) as e:
    print(f'Exception class: {type(e)}')
    print(f'Exception occured: {e}')
</div></details>

<details><summary>
Else節 
※エラーがない場合、除算の結果を表示
</summary><div>
try:
    num = 10 / 5
except ZeroDivisionError:
    print('ZeroDivisionError')
else:
    print(f'除算の結果は{num}です')
</div></details>

<details><summary>
Finally節 
※ファイルfを開いたあとに、存在しない変数dataの中身を書き込む場合
</summary><div>
f = None
try:
    f = open('python.ext', mode='w')
    f.write(date)
finally:
    if f:
        f.close()
        print('ファイルを閉じました)
</div></details>
