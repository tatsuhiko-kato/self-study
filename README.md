# self-study
# 1 Pythonの環境
## 1.1 Pythonパッケージを管理する
### 1.1.1 導入方法
### 1.1.2 基本的な使い方
<details><summary>
パッケージのインストール
（例）sampleprojectをインストール  
</summary><div>
pip install sampleproject
</div></details>

<details><summary>
バージョンを指定したパッケージのインストール
（例）バージョン1.2.0をインストール
</summary><div>
pip install sampleproject==1.2.0
</div></details>

<details><summary>
バージョン範囲を指定したパッケージのインストール
（例）1.2.0以上2.0.0未満のなかで最新のバージョンをインストール
</summary><div>
pip install "sampleproject>=1.2.0<2.0.0
</div></details>

<details><summary>
パッケージのアップグレード
（例）最新バージョンにアップグレード
</summary><div>
pip install --upgrade sampleproject
</div></details>

<details><summary>
パッケージのダウングレード
（例）バージョン1.2.0にダウングレード
</summary><div>
pip install --upgrade sampleproject==1.2.0
</div></details>
