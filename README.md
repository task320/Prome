# Prome
自作のBlog   
まだ記事を並べて表示しかできません。
## Pythonバージョン
- 3.8
## 使用モジュール
以下のモジュールを使用して作っています。   
- flask
- sqlalchemy
- markdown
- jinja2
- psycopg2
## サーバ
nginx -> uwsgi ->アプリ   
の流れでアクセスすることを考えています。

## 実行
```
python src/Run.py
```
## URL
```
http://localhost:5000/contents/all?page=1
```
