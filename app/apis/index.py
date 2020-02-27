# coding=utf-8
from . import Api


@Api.route('/index', methods=["GET"])
def index():
    return 'Index Page'
