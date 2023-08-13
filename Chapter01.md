# self-study
# 1 Pythonの環境
## 1.1 Pythonパッケージを管理する
### 1.1.1 導入方法
### 1.1.2 基本的な使い方
<details>
<summary>
パッケージのインストール ※sampleprojectをインストール 
</summary> 
  
```python
pip install sampleproject
```
</details>

<details>
<summary>
バージョンを指定したパッケージのインストール ※バージョン1.2.0をインストール
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

<details><summary>
パッケージのアップグレード
※最新バージョンにアップグレード
</summary><div>
pip install --upgrade sampleproject
</div></details>

<details><summary>
パッケージのダウングレード
※バージョン1.2.0にダウングレード
</summary><div>
pip install --upgrade sampleproject==1.2.0
</div></details>

<details><summary>
インストールされているパッケージとバージョンの確認
</summary><div>
pip list
</div></details>

<details><summary>
最新版でないパッケージのみ表示
</summary><div>
pip list --outdated
</div></details>

<details><summary>
パッケージのアンインストール
※sampleprojectをアンインストール
</summary><div>
pip uninstall sampleproject
</div></details>

### 1.1.3 requirements.txtを作って、複数の環境でバージョンを統一する
<details><summary>
requirements.txtの作成
</summary><div>
pip freeze > requirements.txt
</div></details>

<details><summary>
requirements.txtを参照してパッケージをインストール
</summary><div>
pip install -r requirements.txt
</div></details>

## 1.2 仮想環境を作成する
### 1.2.2 基本的な使い方
<details><summary>
仮想環境の作成
※envを作成
</summary><div>
python -m venv .env
</div></details>

<details><summary>
仮想環境の作成
※envディレクトリの中身を確認する
</summary><div>
ls -l .env
</div></details>

<details><summary>
仮想環境の有効化
</summary><div>
.env\Scripts\Activate.ps1
</div></details>

<details><summary>
仮想環境のPythonバージョンの確認
</summary><div>
python -V
</div></details>

<details><summary>
仮想環境上でpipを使用
※ pipを最新版にアップグレード
</summary><div>
pip install --upgrade pip
</div></details>

<details><summary>
仮想環境上でpipを使用
※ pipを最新版にアップグレード
</summary><div>
pip install --upgrade pip
</div></details>

<details><summary>
仮想環境上でpipを使用
※ Django==3.2.4をインストール
</summary><div>
pip install Django==3.2.4

</div></details>
