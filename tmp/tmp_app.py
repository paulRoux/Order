from flask import Flask, url_for, request
from common.libs.UrlUtils import UrlManager
from tmp.tmp_route_map import route_order
from flask_sqlalchemy import SQLAlchemy

"""
每次发版有个版本号 201811271629
"""

app = Flask(__name__)
app.register_blueprint(route_order, url_prefix='/order')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Zyy180926.@127.0.0.1/mysql'
track_modifications = app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', True)
db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    url = url_for('index')

    url_1 = UrlManager.build_url('/api')

    url_2 = UrlManager.build_static_url("/css/reset.css")

    msg = f'Hello World! url: {url} ; url_1:{url_1} ; url_2: {url_2}'
    app.logger.error(msg)
    app.logger.info(msg)
    app.logger.debug(msg)
    return msg


@app.route('/api')
def index():
    return 'index page'


@app.route('/api/hello')
def hello():
    from sqlalchemy import text
    sql = text("SELECT * FROM `user`")
    result = db.engine.execute(sql)

    for row in result:
        app.logger.info(row)
    return 'api - hello '


@app.errorhandler(404)
def page_not_found(error):
    app.logger.error(request.path)
    app.logger.error(error)
    return 'this page does not exist', 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
