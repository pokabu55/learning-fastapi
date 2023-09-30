# learning-fastapi
* FastAPIのお勉強用

# 仮想環境の構築
## 普通にvenv使おうとしたらダメだった…
* [参考サイト](https://qiita.com/fiftystorm36/items/b2fd47cf32c7694adc2e)
* 仮想環境の構築 `$ python3 -m venv [newenvname]`
* 仮想環境の有効化
  * `. [newenvname]/bin/activate` と打つ
  * 端末が`$` から `(venv)` に変わる
* 仮想環境の無効化
  * `(venv) $ deactivate` と打つ
  * 端末がもとに戻る
* .gitignore に `venv/` を追加
* 仮想環境を構築しようとする（最初のコマンド）と、file not found error で NG
## 代替手段として virtualenv を使う
* [エラー対処のための virtualenv](https://qiita.com/dyuichi/items/e21d7c7510280cd87944)
* virtualenv と venv の違いは、[こっち](https://envader.plus/course/8/scenario/1075)
* virtualenv の[使い方](https://envader.plus/course/8/scenario/1074)

## virtualenv の使い方
* 仮想環境の構築 `$ python3 -m virtualenv [仮想環境名]`
* or
* `python3 -m virtualenv -p 利用したいPythonのバージョン(例: python3.6) 環境名`
* 仮想環境の有効化
  * `source 仮想環境名/bin/activate` と打つ
  * 端末が`$` から `(仮想環境名)` に変わる
* 仮想環境の無効化
  * `(仮想環境名) deactivate` と打つ
  * 端末がもとに戻る
* python version の確認
  * `(仮想環境名) python -V` と打つ
* パッケージのインストール
  * `(仮想環境名)$ pip install [package-name]`
* 作成した環境にインストールされているパッケージの確認
  * `(仮想環境名)$ pip freeze`
* インストールパッケージのファイル保存 requirements.txt
  * `(仮想環境名)$ pip freeze > requirements.txt`

# FastAPIのインストール
* pip で、fastapi と uvicorn
## uvicorn とは
* 「Uvicorn」(ユビコーン)とは、Python用の「ASGI Webサーバ」実装です。
* 非同期フレームワーク用の低レベル「サーバ/アプリケーション インターフェース」を提供します。
* Uvicornは「HTTP/1.1」＋「WebSocket」をサポートします。
* [参考サイト](https://majisemi.com/topics/oss/4004/#:~:text=%E3%80%8CUvicorn%E3%80%8D(%E3%83%A6%E3%83%93%E3%82%B3%E3%83%BC%E3%83%B3)%E3%81%A8,WebSocket%E3%80%8D%E3%82%92%E3%82%B5%E3%83%9D%E3%83%BC%E3%83%88%E3%81%97%E3%81%BE%E3%81%99%E3%80%82)

# 実装
* api ディレクトリ作成
* `__init__.py` の作成
  * この api ディレクトリがpythonモジュールであることを示す 空ファイル です。
* `main.py` の作成
  * FastAPIのコードを記述します。

# 実行
## API立ち上げ
* api ディレクトリへ移動
* `uvicorn main:app --reload`
* コマンドの意味
  * main: main.pyファイル
  * app: main.py内部で作られるobject (app = FastAPI()の部分)
  * --reload: コード変更時のサーバー再起動
## APIにアクセス
* ブラウザで `http://127.0.0.1:8000`
* SwaggerUIの `http://127.0.0.1:8000/docs`

# 参考サイト
## FastAPIそのもの
* [公式チュートリアル](https://fastapi.tiangolo.com/tutorial/first-steps/)
* [FastAPI入門](https://zenn.dev/sh0nk/books/537bb028709ab9) 例の本の元ネタ
* [PythonでWebAPI作ってみた](https://zenn.dev/riontajima/articles/0aab45b7c99c00)
* [FastAPIで学ぶPythonによるREST API開発の基本](https://zenn.dev/nameless_sn/articles/fastapi_tutorial_for_rest)

## API＋画像処理
* [FastAPIでレシート画像をOCRするAPIサーバを構築する](https://sey323log.hatenablog.com/entry/20220809/1660047905)
* [FastAPIでファイルのアップロードを行う方法](https://senablog.com/python-fastapi-file-upload/)
