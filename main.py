from flask import Flask
from api.endpoint import Endpoint

app = Flask(__name__)

@app.route('/')
def route():
    return 'hcjjhkjcjkcjchk'

app.register_blueprint(Endpoint('messages').blueprint)

if __name__ == '__main__':
    app.run('0.0.0.0')