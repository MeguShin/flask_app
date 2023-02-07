# Flaskモジュールのインポート
from flask import Flask

# Flaskをインスタンス化
app = Flask(__name__)

# ルートディレクトリにアクセスがあった場合、下に書かれているdefから始まる関数を実行
@app.route('/')
def hello():
  return 'Hello World!'

# このプログラムがメインとして実行された場合、app.run()を呼び出す。
if __name__=='__main__':
  # Webアプリケーションの起動
  app.run()