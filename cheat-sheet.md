# 実行手順
* 仮想環境の有効化
  * `source 仮想環境名/bin/activate`
* API立ち上げ
  * api ディレクトリへ移動
  * `uvicorn main:app --reload`
* APIにアクセス
  * `http://127.0.0.1:8000`
  * `http://127.0.0.1:8000/docs` SwaggerUIはこっち
* 仮想環境の無効化
  * `(仮想環境名) deactivate`

# 仮想環境 その他のコマンド
* python version の確認
  * `(仮想環境名) python -V`
* パッケージのインストール
  * `(仮想環境名)$ pip install [package-name]`
* 作成した環境にインストールされているパッケージの確認
  * `(仮想環境名)$ pip freeze`
* インストールパッケージのファイル保存 requirements.txt
  * `(仮想環境名)$ pip freeze > requirements.txt`