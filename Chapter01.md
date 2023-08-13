# self-study
# 1 Pythonの環境
## 1.1 Pythonパッケージを管理する
### 1.1.1 導入方法
### 1.1.2 基本的な使い方
<details>
<summary>
パッケージのインストール  
※sampleprojectをインストール 
</summary> 
  
```python
pip install sampleproject
```
</details>

<details>
<summary>
バージョンを指定したパッケージのインストール  
※バージョン1.2.0をインストール
</summary>

```python
pip install sampleproject==1.2.0
```
</details>

<details>
<summary>
バージョン範囲を指定したパッケージのインストール  
※1.2.0以上2.0.0未満のなかで最新のバージョンをインストール
</summary>

```python
pip install "sampleproject>=1.2.0<2.0.0"
```
</details>

<details>
<summary>
パッケージのアップグレード  
※最新バージョンにアップグレード
</summary>

```python
pip install --upgrade sampleproject
```
</details>

<details>
<summary>
パッケージのダウングレード  
※バージョン1.2.0にダウングレード
</summary>

```python
pip install --upgrade sampleproject==1.2.0
```
</details>

<details>
<summary>
インストールされているパッケージとバージョンの確認
</summary>

```python
pip list
```
</details>

<details>
<summary>
最新版でないパッケージのみ表示
</summary>

```python
pip list --outdated
```
</details>

<details>
<summary>
パッケージのアンインストール  
※sampleprojectをアンインストール
</summary>

```python
pip uninstall sampleproject
```
</details>

### 1.1.3 requirements.txtを作って、複数の環境でバージョンを統一する
<details>
<summary>
requirements.txtの作成
</summary>

```python
pip freeze > requirements.txt
```
</details>

<details>
<summary>
requirements.txtを参照してパッケージをインストール
</summary>

```python
pip install -r requirements.txt
```
</details>

## 1.2 仮想環境を作成する
### 1.2.2 基本的な使い方
<details>
<summary>
仮想環境の作成  
※envを作成
</summary>

```python
python -m venv .env
```
</details>

<details>
<summary>
仮想環境の作成  
※envディレクトリの中身を確認する
</summary>

```python
ls -l .env
```
</details>

<details>
<summary>
仮想環境の有効化
</summary>

```python
.env\Scripts\Activate.ps1
```
</details>

<details>
<summary>
仮想環境のPythonバージョンの確認
</summary>

```python
python -V
```
</details>

<details>
<summary>
仮想環境上でpipを使用  
※ pipを最新版にアップグレード
</summary>

```python
pip install --upgrade pip
```
</details>

<details>
<summary>
仮想環境上でpipを使用  
※ pipを最新版にアップグレード
</summary>

```python
pip install --upgrade pip
```
</details>

<details>
<summary>
仮想環境上でpipを使用  
※ Django==3.2.4をインストール
</summary>

```python
pip install Django==3.2.4
```

</details>
