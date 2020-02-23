# -*- coding: utf-8 -*-
from app import *
from app.modules.redisd import Redis
from app.modules.Ldap import Ldap
from app.modules.mysqld import Role
import functools

redis = Redis()
ldap = Ldap()


@app.before_request
def before_request():
    pass


def access_auth(func):

    """
    用户权限验证的装饰器
    :param func:
    """
    @functools.wraps(func)
    def decorated_view(*args, **kwargs):
        print(func.__name__)
        return func(*args, **kwargs)
    return decorated_view


def authority_cache():
    Role.query.all()
