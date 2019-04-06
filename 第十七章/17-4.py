import flask
app = flask.Flask(__name__)

@app.route('/hello/<name>')
def helo(name):
    return '你好' +name +'!'
if __name__ == '__main__':
    app.run()