# -*- coding: utf-8 -*-
from app import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(threaded=True, host=app.config['BIND'], port=app.config['PORT'], debug=app.config['DEBUG'])
