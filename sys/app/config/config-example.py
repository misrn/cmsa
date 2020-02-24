# -*- coding: utf-8 -*-

BIND = '0.0.0.0'
PORT = 5000

DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
CSRF_ENABLED = True
SECRET_KEY = 'asdfghjkl'

# 数据库配置
SQLALCHEMY_POOL_SIZE = 100
SQLALCHEMY_POOL_RECYCLE = 10
SQLALCHEMY_POOL_TIMEOUT = 3000
SQLALCHEMY_DATABASE_URI = 'mysql://root:password@127.0.0.1:3306/cmsa'


# failed_max: 登录最大失败次数; lock_time:达到最大次数锁定时间,单位秒
LOGIN_CONFIG = {
    'failed_max': 3,
    'lock_time': 600
}

# REDIS配置
REDIS_CONFIG = {
    'host': '127.0.0.1',
    'port': 6379,
    'db': 9,
    'password': 'password'
}


# LDAP服务器配置
LDAP_CONFIG = {
    'host': 'ldap://127.0.0.1:389',
    'base_dn': 'dc=test,dc=cn',
    'people_dn': 'ou=People,dc=test,dc=cn',
    'user': 'cn=Manager,dc=test,dc=cn',
    'password': 'password',
    'login': True
}
