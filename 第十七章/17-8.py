# -*- encoding:utf-8 -*-
import flask
app = flask.Flask(__name__)
@app.route('/hello')
def helo():
    return flask.render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)