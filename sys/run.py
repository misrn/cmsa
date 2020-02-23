# -*- coding: utf-8 -*-
from app import app

if __name__ == '__main__':
    app.run(threaded=True, host=app.config['BIND'], port=app.config['PORT'])
