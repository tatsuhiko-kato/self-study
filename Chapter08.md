# self-study
# 8 日付と時刻の処理
## 8.1 日付や時刻を扱う - datetime
### 8.1.1 日付を扱う - dateオブジェクト

```python
from datetime import date
g = date(2021, 1, 1) # 元日
# 年・月・日を取得してタプルで表示
# 曜日を取得
# isoフォーマットに変換
# isoフォーマットの文字列で日付'2021-01-01'を指定し、isodateに格納
# 日付をスラッシュ区切りの文字列に変換
# 日付を月、曜日の文字列付きで変換
# 現在の日付を取得
# f-stringで「今日はYYYY年MM月DD日」に変換
```

<details>
<summary>
dateのサンプルコード
</summary>

```python
from datetime import date
g = date(2021, 1, 1) # 元日

# 年・月・日を取得してタプルで表示
>>> g.year, g.month, g.day
(2021, 1, 1)

# 曜日を取得
>>> g.weekday()
4

# isoフォーマットに変換
>>> g.isoformat()
'2021-01-01'

# isoフォーマットの文字列で日付'2021-01-01'を指定し、isodateに格納
>>> isodate = date.fromisoformat('2021-01-01')
>>> isodate
datetime.date(2021, 1, 1)

# 日付をスラッシュ区切りの文字列に変換
>>> g.strftime('%Y/%m/%d')
'2021/01/01'

# 日付を月、曜日の文字列付き（2021 Jan 01 Fri)に変換
>>> g.strftime('%Y %b %d %a')
'2021 Jan 01 Fri'

# 現在の日付を取得
>>> date.today()
datetime.date(2023, 8, 15)

# f-stringで「今日はYYYY年MM月DD日」に変換
>>> f'今日は{date.today():%Y年%m月%d日}'
'今日は2023年08月15日'
```
</details>


### 8.1.2 時刻を扱う - timeオブジェクト

```python
from datetime import time
# 0時0分
# 16時12分25秒
# 10分
# 10秒
# 10ミリ秒
# 16時12分25秒をnowに格納
# nowの時、分、秒、ミリ秒を取得してタプルで表示
# nowをisoformatで表示
# isoformatの文字列'16:12:25'を読み込み
# isoformatの文字列'16:12:25.000384'を読み込み
# isoformatの文字列'16:12:25+04:00'を読み込み
# 現在時刻をHH:MM形式で表示
```

<details>
<summary>
timeのサンプルコード
</summary>

```python
from datetime import time
# 0時0分
>>> time()
datetime.time(0, 0)

# 16時12分25秒
>>> time(16, 12, 25)
datetime.time(16, 12, 25)

# 10分
>>> time(minute=10)
datetime.time(0, 10)

# 10秒
>>> time(second=10)
datetime.time(0, 0, 10)

# 10ミリ秒
>>> time(microsecond=10)
datetime.time(0, 0, 0, 10)

# 16時12分25秒をnowに格納し、時、分、秒、ミリ秒を取得してタプルで表示
>>> now = time(16, 12, 25)
>>> now.hour, now.minute, now.second, now.microsecond
(16, 12, 25, 0)

# nowをisoformatで表示
>>> now.isoformat()
'16:12:25'

# isoformatの文字列'16:12:25'を読み込み
>>> time.fromisoformat('16:12:25')
datetime.time(16, 12, 25)

# isoformatの文字列'16:12:25.000384'を読み込み
>>> time.fromisoformat('16:12:25.000384')
datetime.time(16, 12, 25, 384)

# isoformatの文字列'16:12:25+04:00'を読み込み
>>> time.fromisoformat('16:12:25+04:00')
datetime.time(16, 12, 25, tzinfo=datetime.timezone(datetime.timedelta(seconds=14400)))

# nowをHH:MM形式で表示
>>> now.strftime('%H:%M')
'16:12'
```
</details>

### 8.1.3 日時を扱う - datetimeオブジェクト

```python
from datetime import datetime
# 現在日時を取得し、nowに格納
# nowのdateを取得
# nowのtimeを取得
# ISO 8601形式の文字列を取得
# ISO 8601形式の文字列'2021-02-14'をdatetime型に格納
# ISO 8601形式の文字列'2021-02-14T00:05:23'をdatetime型に格納
# ISO 8601形式の文字列'2021-02-14T17:26:08.585404'をdatetime型に格納
# nowをYYYY/MM/DDフォーマットの文字列として出力
# 文字列'2021/01/14'をdatetimeオブジェクトに変換
from zoneinfo import ZoneInfo
# 2021/05/24 22:50:0.0 timezone='sia/Tokyo'でdatetimeオブジェクトに変換
```

<details>
<summary>
datetimeのサンプルコード
</summary>

```python
>>> from datetime import datetime
# 現在日時を取得し、nowに格納
>>> now = datetime.now()

# nowのdateを取得
>>> now.date()
datetime.date(2023, 8, 15)

# nowのtimeを取得
>>> now.time()
datetime.time(4, 28, 23, 920065)

# ISO 8601形式の文字列を取得
>>> now.isoformat()
'2023-08-15T04:28:23.920065'

# ISO 8601形式の文字列'2021-02-14'をdatetime型に格納
>>> datetime.fromisoformat('2021-02-14')
datetime.datetime(2021, 2, 14, 0, 0)

# ISO 8601形式の文字列'2021-02-14T00:05:23'をdatetime型に格納
>>> datetime.fromisoformat('2021-02-14T00:05:23')
datetime.datetime(2021, 2, 14, 0, 5, 23)

# ISO 8601形式の文字列'2021-02-14T17:26:08.585404'をdatetime型に格納
>>> datetime.fromisoformat('2021-02-14T17:26:08.585404')
datetime.datetime(2021, 2, 14, 17, 26, 8, 585404)

# nowをYYYY/MM/DDフォーマットの文字列として出力
>>> now.strftime('%Y/%m/%d')
'2023/08/15'

# 文字列'2021/01/14'をdatetimeオブジェクトに変換
>>> datetime.strptime('2021/01/14', '%Y/%m/%d')
datetime.datetime(2021, 1, 14, 0, 0)

# 2021/05/24 22:50:0.0 timezone='Asia/Tokyo'でdatetimeオブジェクトに変換
>>> from zoneinfo import ZoneInfo
>>> datetime(2021, 5, 24, 22, 50, 0, 0, tzinfo=ZoneInfo('Asia/Tokyo'))
datetime.datetime(2021, 5, 24, 22, 50, tzinfo=zoneinfo.ZoneInfo(key='Asia/Tokyo'))
```
</details>

### 8.1.4 日時の差を扱う - timedeltaオブジェクト

```python
# 今日の日付を取得してtodayに格納
from datetime import date, datetime, time, timedelta
# 来年の元旦をnewyearsdayに格納
# 今日から来年の元旦までの日数
# 1週間のtimedeltaをweekに格納
# 1週間後の日付を取得
# 2週間後の日付を取得
# 1週間前の日付を取得
# 2021/05/24 21:00:00.0と2021/05/24 20:00:00.0の差分（秒表示）
```

<details>
<summary>
timedeltaのサンプルコード
</summary>

```python
# 今日の日付を取得してtodayに格納
>>> today = date.today()
>>> from datetime import date, datetime, time, timedelta

# 来年の元旦をnewyearsdayに格納し、今日から来年の元旦までの日数を出力
>>> newyearsday = date(2024, 1, 1)
>>> newyearsday - today
datetime.timedelta(days=139)

# 1週間のtimedeltaをweekに格納し、1週間後の日付を出力
datetime.timedelta(days=139)
>>> week = timedelta(days=7)
>>> today + week
datetime.date(2023, 8, 22)

# 2週間後の日付を出力
>>> today + week * 2
datetime.date(2023, 8, 29)

# 1週間前の日付を出力
>>> today - week
datetime.date(2023, 8, 8)

# 2021/05/24 21:00:00.0と2021/05/24 20:00:00.0の差分（秒表示）
>>> datetime(2021, 5, 24, 21, 0, 0, 0) - datetime(2021, 5, 24, 20, 0, 0, 0)
datetime.timedelta(seconds=3600)
```
</details>

### 8.1.5 strftome()で使える主な指定子
### 8.1.6 datetime：よくある使い方
### 8.1.7 datetime：ちょっと役立つ周辺知識
### 8.1.8 datetime：よくあるエラーと対処法

## 8.2 時刻を扱う - time
### 8.2.1 時刻を取得する

```python
# UTCの現在時刻を出力
import time
# ローカルの現在時刻を出力
# ローカルの現在時刻をYYYY-MM-DD形式で出力
# エポックからの秒数を浮動小数点で出力
```

<details>
<summary>
時刻を取得する
</summary>

```python
# UTCの現在時刻を出力
>>> import time
>>> time.gmtime()
time.struct_time(tm_year=2023, tm_mon=8, tm_mday=15, tm_hour=5, tm_min=0, tm_sec=44, tm_wday=1, tm_yday=227, tm_isdst=0)

# ローカルの現在時刻を出力
>> time.localtime()
time.struct_time(tm_year=2023, tm_mon=8, tm_mday=15, tm_hour=5, tm_min=1, tm_sec=15, tm_wday=1, tm_yday=227, tm_isdst=0)

# ローカルの現在時刻をYYYY-MM-DD形式で出力
>>> time.strftime('%Y-%m-%d', time.localtime())
'2023-08-15'

# エポックからの秒数を浮動小数点で出力
>>> time.time()
1692075750.032333
```

</details>

### 8.2.2 時刻オブジェクト - struct_time

```python
import time
# ローカルの現在時刻をlocalに格納
# UTCの現在時刻をutcに格納
# ローカルのタイムゾーンとオフセットを出力
# UTCのタイムゾーンとオフセットを出力
```

<details>
<summary>
struct_timeのサンプルコード
</summary>

```python
import time
# ローカルの現在時刻をlocalに格納、ローカルのタイムゾーンとオフセットを出力
>>> local = time.localtime()
>>> local.tm_zone, local.tm_gmtoff
('JST', 32400)

# UTCの現在時刻をutcに格納
# UTCのタイムゾーンとオフセットを出力
```

</details>

### 8.2.3 スレッドの一時停止
### 8.2.4 time：よくある使い方
### 8.2.5 time：ちょっと役立つ周辺知識

## 8.3 IANAタイムゾーンデータベースを扱う - zoneinfo
### 8.3.1 IANAタイムゾーンを表すオブジェクト - ZoneInfo

```python
from zoneinfo import ZoneInfo
# 日本時間で2021年2月23日10:00のdatetimeオブジェクトをdtに格納
# 'America/Los_Angeles'タイムゾーンに変換して出力
```

<details>
<summary>
zoneinfo.ZoneInfoの使用例
</summary>

```python
# 日本時間で2021年2月23日10:00のdatetimeオブジェクトをdtに格納
>>> from zoneinfo import ZoneInfo
>>> dt = datetime(2021, 2, 23, 10, 0, 0, tzinfo=ZoneInfo(key='Asia/Tokyo'))
>>> dt
datetime.datetime(2021, 2, 23, 10, 0, tzinfo=zoneinfo.ZoneInfo(key='Asia/Tokyo'))

# 'America/Los_Angeles'タイムゾーンに変換して出力
>>> dt.astimezone(ZoneInfo('America/Los_Angeles'))
datetime.datetime(2021, 2, 22, 17, 0, tzinfo=zoneinfo.ZoneInfo(key='America/Los_Angeles'))
```

</details>

### 8.3.2 zoneinfo：よくある使い方
### 8.3.3 zoneinfo：ちょっと役立つ周辺知識
### 8.3.4 zoneinfo：よくあるエラーと対処法
