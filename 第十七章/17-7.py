# -*- encoding:utf-8 -*-

import flask
html_txt = '''
<!DOCTYPE html>
<html>
    <body>
        <h2>收到GET请求</h2>
        <a href = '/get_info'>获取会话信息</a>
    </body>
</html>
'''
app = flask.Flask(__name__)
@app.route('/set_info/<name>')
def set_cks(name):
    name  = name if name else  'anonymous'
    flask.session['name'] = name
    return html_txt
@app.route('/get_info')
def get_cks():
    name = 'name' in flask.session and flask.session['name']
    if name:
        return '获取的会话信息：'+name
    else:
        return '没有相应的会话信息。'
if __name__ == '__main__':
    app.secret_key = 'dfafff#sakdjgsdjgsksdsakldjhgj'
    app.run(debug=True)
