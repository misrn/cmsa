# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import logging

app = Flask(__name__)
CORS(app)

app.config.from_pyfile('config/config.py')
db = SQLAlchemy(app)

# 日志配置
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger()

from app.views import manage, menus

# 路由
app.register_blueprint(manage.Manage, url_prefix='/')
app.register_blueprint(menus.Menu, url_prefix='/api/menu')
