# self-study
# 13 特定のデータフォーマットを扱う
## 13.1 csvファイルを扱う
### 13.1.1 csvファイルの読み込みと書き込み

```python
import csv
# UTF-8エンコーディングで作成されたファイル13_01_01_sample.csvを１行ずつ読み込んで出力
```

<details><summary>sample code</summary>

```python
>>> import csv

# UTF-8エンコーディングで作成されたファイル13_01_01_sample.csvを１行ずつ読み込んで出力
>>> with open('13_01_01_sample.csv', mode='r', encoding='utf-8') as f:
...     reader = csv.reader(f)
...     for row in reader:
...         print(row)
... 
['id', '都道府県', '人口（人）', '面積（km2）']
['1', '東京都', '13900000', '2194.05']
['2', '神奈川県', '9200000', '2416.10']
['3', '千葉県', '6200000', '5157.50']
['4', '埼玉県', '7300000', '3797.75']

```

</details>

```python
import csv
# デリミターをタブ、引用符を#で作成されたファイル13_01_01_sample.tsvを１行ずつ読み込んで出力
```

<details><summary>sample code</summary>

```python
>>> import csv

# デリミターをタブ、引用符を#で作成されたファイル13_01_01_sample.tsvを１行ずつ読み込んで出力
>>> with open('13_01_01_sample.tsv', mode='r') as f:
...     reader = csv.reader(f, delimiter='\t', quotechar='#')
...     for row in reader:
...         print(row)
... 
['都道府県', '人口密度']
['東京都', '6335']
['埼玉県', '1922']
```

</details>

ファイルの読み込みと加工、出力
```python
import csv

with open('13_01_01_sample.csv', mode='r', encoding='utf-8') as read_file:
    reader = csv.reader(read_file)
    next(reader)  # ヘッダー行を飛ばす
    with open('13_01_01_result.tsv', newline='', mode='w', encoding='utf-8') as write_file:
        writer = csv.writer(write_file, delimiter='\t')
        writer.writerow(['都道府県', '人口密度'])
        for row in reader:
            population_density = float(row[2]) / float(row[3])
            writer.writerow([row[1], int(population_density)])
```

### 13.1.2 辞書データを用いたCSVファイルの読み込みと書き込み

```python
>>> import csv
>>> with open('13_01_01_sample.csv', mode='r', encoding='utf-8') as f:
...     for row in csv.DictReader(f):
...         print(row)
... 
{'id': '1', '都道府県': '東京都', '人口（人）': '13900000', '面積（km2）': '2194.05'}
{'id': '2', '都道府県': '神奈川県', '人口（人）': '9200000', '面積（km2）': '2416.10'}
{'id': '3', '都道府県': '千葉県', '人口（人）': '6200000', '面積（km2）': '5157.50'}
{'id': '4', '都道府県': '埼玉県', '人口（人）': '7300000', '面積（km2）': '3797.75'}
```

### 13.1.3 csv：よくある使い方
### 13.1.4 csv：ちょっと役立つ周辺知識
### 13.1.5 csv：よくあるエラーと対処法

## 13.2JSONを扱う
### 13.2.1 JSONのエンコードとデコード

JSONエンコード
```python
>>> import json
>>> data = [{'id': 123, 'entities': {'url': 'python.org', 'hashtags': ['#python', '#pythonjp']}}]
>>> print(json.dumps(data, indent=2))
[
  {
    "id": 123,
    "entities": {
      "url": "python.org",
      "hashtags": [
        "#python",
        "#pythonjp"
      ]
    }
  }
]
```

JSONデコード
```python
>>> from decimal import Decimal
>>> json_str = '["ham", 1, "egg", 1.0, {"a":false, "b":null}]'
>>> json.loads(json_str)
['ham', 1, 'egg', 1.0, {'a': False, 'b': None}]
```

### 13.2.2 JSONのエンコードとデコード（ファイルオブジェクト）
### 13.2.3 json：よくある使い方
### 13.2.4 json：ちょっと役立つ周辺知識
### 13.2.5 json：よくあるエラーと対処法

