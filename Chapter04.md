# self-study
# 4 Pythonのクラス
## 4.1 class構文
### 4.1.1 クラス定義

```python
'''
Userクラス
データ属性としてuser_typeを初期値Noneで宣言
インスタンス変数name, age, addressにコンストラクター引数の値を代入
年齢を１つ増やすincrement_ageのメソッドを定義
nameを１文字目を返す（nameがブランクの場合は""を返す）start_nameメソッドを定義
'''
```
<details>
<summary>
Userクラスの定義
</summary>

```python
class User:
    user_type = None

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def increment_age(self):
        self.age += 1

    def start_name(self):
        if len(self.name) > 0:
            return self.name[0]
        else:
            return ""
        
```
</details>

```python
user1 = User("寺田学", 35, "東京都台東区")
user2 = User("鈴木たかのり", 30, "東京都渋谷区")
```
<details>
<summary>
user1のageを表示し、1つ増やした後で再表示
</summary>

```python
user1.age
user1.increment_age()
user1.age
```
</details>

### 4.1.3 selfとは

## 4.2 属性とメソッド
### 4.2.1 コンストラクター
### 4.2.2 データ属性
<details>
<summary>
クラス変数user_typeへのアクセス
</summary>
User.user_type
</details>

<details>
<summary>
インスタンスuser1のインスタンス変数nameへのアクセス
</summary>
user1.name
</details>

### 4.2.3 メソッド

### 4.2.4 特殊メソッド

```python
__init__  # コンストラクター
__call__  # 呼び出し可能化
__repr__  # 文字列表現
__str__  # 文字列型への変換
__len__  # 要素数の取得
__lt__  # 小なり比較＜比較演算子
__le__ # 以下比較＜＝比較演算子
__eq__  # 等価比較＝＝比較演算子
__ne__  # 非等価比較！＝比較演算子
__gt__  # 大なり比較＞比較演算子
__ge__  # 以上比較＞＝比較演算子
__add__  # 加算演算＋算術演算子
__sub__  # 減算演算ー算術演算子
__mul__  # 乗算演算＊算術演算子
__truediv__  # 除算演算／算術演算子 

```

### 4.2.5 プロパティ化

<details>
<summary>
nameの先頭文字を返すメソッドをプロパティ化
</summary>

```python
@property
def start_name(self):
    return(self.name[0])

user.start_name

```
</details>

### 4.2.6 クラスメソッドの具体的な使い方

## 4.3 継承
### 4.3.1 標準ライブラリの継承の例
### 4.3.2 子クラスの定義
### 4.3.3 多重継承
### 4.3.4 継承：よくある使い方
### 4.3.5 エラーと対処方法

## 4.4 dataclass
### 4.4.1 基本文法

```python
class User:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    
    def __repr__(self):
        return f"User(name='{self.name}', age={self.age}, address='{self.address}')")
```

<details>
<summary>
クラスデコレーターでdetaclassを宣言、クラス変数(name, age, address)を宣言、型ヒント(str, int, str)を宣言
</summary>

```python
from dataclass import dataclass

@dataclass
class User:
    name: str
    age: int
    address: str
```
</details>

### 4.4.2 コンストラクターの任意引数

<details>
<summary>
任意引数activeをbool型、デフォルト値Falseで宣言
</summary>

```python
from dataclass import dataclass

@dataclass
class User:
    name: str
    age: int
    address: str
    active: bool = False
```
</details>

### 4.4.3 データ変換

<details>
<summary>
dataclassで宣言したクラスのデータ属性を辞書に変換
</summary>
asdict(instance)
</details>

<details>
<summary>
dataclassで宣言したクラスのデータ属性をタプルに変換
</summary>
astuple(instance)
</details>

### 4.4.4 dataclass：よくある使い方
### 4.4.5 エラーと対処方法

## 4.5 オブジェクト関連関数
### 4.5.1 関数の種類

```python
id(object)  # 識別値を整数で返す
type(object)  # 型オブジェクトを返す
isinstance(object, classinfo)  # objectがclassinfoのインスタンスであるか判定する
issubclass(class, classinfo)  # classがclassinfoのサブクラスであるか判定する
help(object)  # objectのヘルプを表示する
dir(object)  # objectが持つ属性・メソッドのリストを返す
```

### 4.5.2 オブジェクト関連関数の使い方

<details>
<summary>
summary
</summary>
details
</details>
