import flask
app = flask.Flask(__name__)
@app.route('/')
@app.route('/hello')
def helo():
    return '你好，我是Flask'
if __name__ == '__main__':
    app.run()