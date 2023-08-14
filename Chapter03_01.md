# self-study
# 3 Pythonの言語仕様
## 3.1 例外処理
### 3.1.1 例外を処理する
<details>
<summary>
例外を発生させる ※ゼロで割る
</summary>

```python
num = 0 / 10
```
</details>

<details>
<summary>
try-except ※ZeroDivisionErrorのハンドリング 
</summary>

```python
try:
    num = 10 / 0
    print(f'除算の結果は{num}になります')
except ZeroDivisionError:
    print('0で割ることはできません')
```
</details>

<details>
<summary>
複数の例外を補足する ※ZeroDivisionError, TypeError
</summary>

```python
try:
    num = 10 / '2'
    print(f'除算の結果は{num}になります')
except ZeroDivisionError:
    print('0で割ることはできません')
except TypeError:
    print('文字列で割ることはできません')
```
</details>

<details>
<summary>
複数の例外を補足する ※ZeroDivisionError, TypeError, NameError内容を一時変数で受け取ってexcept節のなかで利用
</summary>

```python
try:
    num = 10 / 0
except (ZeroDivisionError, TypeError, NameError) as e:
    print(f'Exception class: {type(e)}')
    print(f'Exception occured: {e}')
```
</details>

<details>
<summary>
Else節 ※エラーがない場合、除算の結果を表示
</summary>

```python
try:
    num = 10 / 5
except ZeroDivisionError:
    print('ZeroDivisionError')
else:
    print(f'除算の結果は{num}です')
```
</details>

<details>
<summary>
Finally節 ※ファイルfを開いたあとに、存在しない変数dataの中身を書き込む場合
</summary>

```python
f = None
try:
    f = open('python.ext', mode='w')
    f.write(date)
finally:
    if f:
        f.close()
        print('ファイルを閉じました)
```
</details>

### 3.1.2 基底クラスで例外を補足する
<details>
<summary>
基底クラスで例外を補足する ※ZeroDivisionErrorを基底クラスで補足する
</summary>

```python
try:
    num = 10 / 0
except ArithmeticError as e:
    print(f' Exception class: {type(e)}')
    print(f' Exception description: {e}')
# 基底クラスで補足しても実際の例外クラスのZeroDivisionErrorが渡される
```
</details>

### 3.1.3 独自の例外を定義して、例外を送出する
<details>
<summary>
独自の例外を定義する ※Exceptionクラスを継承
</summary>

```python
class MyError(Exception): 
    pass

raise myError('MyError が発生しました')
'''
Traceback (most recent call last):   
  File "<stdin>", line 1, in <module>
__main__.MyError: MyErrorが発生しました
'''
```
</details>

### 3.1.4 例外処理: よくある使い方
<details>
<summary>
titleとdetailの属性を持ち、詳細なエラー情報を取り出せるMyValidationErrorという基底クラスを作成
</summary>

```python
class MyValidationError(Exception):
    '''MyValidationError
    '''
    title = None
    detail = None

    def __str__(self):
        return str(self.title)


class MyTypeError(MyValidationError):
    '''MyTypeError
    '''
    title = 'Type error'
    detail = '数値で入力してください'


class MyMaxError(MyValidationError):
    '''MyMaxError
    '''
    title = 'Max error'
    detail = 'Max100までの値を入力してください'


def validate_number(num):
    '''validate_number
    '''
    try:
        num = int(num)
    except ValueError:
        raise MyTypeError
    if num > 100:
        raise MyMaxError

try:
    input_number = input('検証する数値を入力してください=>')
    validate_number(input_number)
except MyValidationError as e:
    print(f'{e}の例外が発生しました')
    print(f'detail={e.detail}')
```
</details>

### 3.1.5 例外処理: ちょっと役立つ周辺知識

### 3.1.6 例外処理: よくあるエラーと対処法
<details>
<summary>
悪い例 ※try文で囲む範囲が広すぎるため、可読性が下がり、エラー原因の特定が難しくなる
</summary>

```python
import csv

try:
    input_file_name = input('Enter file_name:')
    with open(input_file_name, mode='r') as f:
        reader = csv.reader(f)
        for row in reader:
            population_density = float(row[1]) / float(row[2])
            print(f'{row[0]}の人口密度は{population_density}です')
except:
    print('例外が発生しました')
```
</details>

<details>
<summary>
良い例
</summary>

```python
import csv

input_file_name = input('Enter file_name:') # try節から外だし
try:
    with open(input_file_name, mode='r') as f:
        reader = csv.reader(f)
        for row in reader:
            population_density = float(row[1]) / float(row[2])
            print(f'{row[0]}の人口密度は{population_density}です')
except FileNotFoundError:
    print(f'ファイルがありません')
except ZeroDivisionError:
    print(f'{row[0]}:{row[1]}, {row[2]} => 値0は指定できません')
except ValueError:
    print(f'{row[0]}:{row[1]}, {row[2]} => 数値以外は指定できません')
```
</details>