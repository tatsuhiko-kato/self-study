# self-study
# 14 インターネット上のデータを扱う
## 14.1 URLをパースする
### 14.1.1 URLをパースする

```python
>>> from urllib import parse
>>> result = parse.urlparse('https://www.example.com/test/;parameter?q=example#hoge')
>>> result
ParseResult(scheme='https', netloc='www.example.com', path='/test/', params='parameter', query='q=example', fragment='hoge')

>>> result.geturl()
'https://www.example.com/test/;parameter?q=example#hoge'

```

### 14.1.2 クエリ文字列をパースする

```python
>>> result.geturl()
'https://www.example.com/test/;parameter?q=example#hoge'
>>> result = parse.urlparse('https://www.google.co.jp/search?q=python&oq=python&sourceid=chrome&ie=UTF-8')
>>> result.query
'q=python&oq=python&sourceid=chrome&ie=UTF-8'
>>> parse.parse_qs(result.query)
{'q': ['python'], 'oq': ['python'], 'sourceid': ['chrome'], 'ie': ['UTF-8']}
```

### 14.1.3 クエリ文字列を組み立てる

```python
>>> parse.urlencode({'key1':1, 'key2':2, 'key3':'ぱいそん'})
'key1=1&key2=2&key3=%E3%81%B1%E3%81%84%E3%81%9D%E3%82%93'
```
### 14.1.4 URLとして使用できる文字列に変換する
### 14.1.5 URLを結合する
### 14.1.6 urllib.parse：よくある使い方
### 14.1.7 urllib.parse：よくあるエラーと対処法

## 14.2 URLを開く
### 14.2.1 指定のURLを開く

GETメソッドを使用したリクエスト
```python
>>> from urllib import request
>>> with request.urlopen('https://httpbin.org/get') as f:
...     res = f.read()[:92]
... 
>>> res
b'{\n  "args": {}, \n  "headers": {\n    "Accept-Encoding": "identity", \n    "Host": "httpbin.org'

```

POSTメソッドを使用したリクエスト

```python
>>> data = 'key1=value1&key2=value2'
>>> res = request.urlopen('https://httpbin.org/post', data=data.encode())
>>> res.status
```

### 14.2.2 GET, POST以外のHTTPメソッドを扱う
### 14.2.3 レスポンスモジュール
### 14.2.4 urllib.request：よくある使い方
### 14.2.5 urllib.request：ちょっと役立つ周辺知識
### 14.2.6 urllib.request：よくあるエラーと対処法

## 14.4 Base16, Base64などへエンコードする
### 14.4.1 Base64にエンコードする
### 14.4.2 Base64からデコードする
### 14.4.3 Base64：よくある使い方
### 14.4.4 Base64：ちょっと役立つ周辺知識
