from flask import Flask
from flask import request
from flask import abort

from flask import session
from flask_script import Manager

from models import db
from utils import format_time
from utils import gen_csrf_token

app = Flask(__name__)
manager = Manager(app)


def configured_app():
    app.config.from_object('config')
    db.init_app(app)
    register_routes(app)
    configure_log(app)
    configure_env_vars(app)
    return app


def register_routes(app):
    from routes.todo import main as routes_todo
    app.register_blueprint(routes_todo)


def configure_log(app):
    # 但是如果 app 是 debug 模式的话, 则不用这么搞
    if not app.debug:
        import logging
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename='logs/todo.log',
                            filemode='a')


def configure_env_vars(app):
    app.jinja_env.filters['format_time'] = format_time
    app.jinja_env.globals['csrf_token'] = gen_csrf_token


@app.before_request
def csrf_protect():
    if request.method == 'POST':
        token = session.pop('_csrf_token', '')
        if not token or token != request.form.get('_csrf_token'):
            abort(403)


@manager.command
def server():
    app = configured_app()
    config = dict(
        debug=False,
        host='127.0.0.1',
        port=3000,
    )
    app.run(**config)


def main():
    manager.run()


if __name__ == '__main__':
    main()
