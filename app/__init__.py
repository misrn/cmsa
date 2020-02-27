# -*- coding: utf-8 -*-
from flask import Flask
import logging


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
        # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config/config.py')

    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # 日志配置
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logging.getLogger()
    # 数据库配置

    #
    # from app.views import manage, menus
    #
    # # 路由
    from app.apis import Api
    app.register_blueprint(Api, url_prefix='/api')
    return app
