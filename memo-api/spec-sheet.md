# RESTAPI
* RESTAPIに従ってTODOアプリを実現するのに必要な機能
* REST APIでは、`HTTPメソッド エンドポイント（{}内はパラメータ）`の形式で書く
* と、以下のように定義

|機能|REST API|
|---|---|
|TODOリストを表示する|GET /tasks |
| TODOにタスクを追加する| POST /tasks |
| TODOのタスクの説明文を変更する| PUT /tasks/{task_id}|
| TODOのタスク自体を削除する| DELETE /tasks/{task_id} |
| TODOタスクに「完了」フラグを立てる| PUT /tasks/{task_id}/done|
| TODOタスクから「完了」フラグを外す| DELETE /tasks/{task_id}/done|

## Routers
* ルーター（routers）に、上記定義にパスオペレーション関数を定義していきます。
* パスオペレーション関数は、
  * 「パス」と「オペレーション」の組み合わせで定義
* 上記のREST APIにおける、
  * 「エンドポイント」と「HTTPメソッド」にそれぞれ対応します。

# ディレクトリ構造
```
api
├── __init__.py
├── main.py
├── schemas
│   └── __init__.py
├── routers
│   └── __init__.py
├── models
│   └── __init__.py
└── cruds
    └── __init__.py
```

# パスオペレーション関数の作成
* 今回のTODOアプリの場合、 `/tasks` と `/tasks/{task_id}/done` の２つのリソースに大別できる
* それぞれを、 `api/routers/task.py` と `api/routers/done.py` に書いていく