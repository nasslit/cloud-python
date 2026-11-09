import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
return "Приложение работает в облаке! Версия 2 успешно запущена!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
