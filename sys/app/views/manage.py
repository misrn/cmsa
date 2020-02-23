# -*- coding: utf-8 -*-
from flask import Blueprint, request
from app.views.common import *
from app.modules.mysqld import User
import logging
import datetime
import uuid
import json

Manage = Blueprint('manage', __name__)


@Manage.route('/login', methods=["POST"])
def login():
    """
    用户登录请求接口 {"username":"{{username}}","password":"{{password}}"}:
    逻辑：
    1.判断连接ldap服务器判断用户名/密码是否正确 ， {错误} 返回账户密码错误
    2.在数据库中查询用户是否存在，{存在}，更新login_time时间，返回认证成功
    3.向LDAP服务器查询用户基础信息，插入数据库
    :return:
    """
    try:
        data = json.loads(request.get_data())
        user_name = data["username"]
        password = data["password"]
        user_login_lock_redis_key = user_name + '_login_lock'
        token = str(uuid.uuid1())

        if redis.exists(user_login_lock_redis_key):
            if int(redis.get(user_login_lock_redis_key)) >= 3:
                logging.debug("用户: " + str(user_name + " 密码连续输入错误已达限制"))
                return json.dumps({"code": 406, "msg": "账户密码连续输入错误已达限制，请稍后再试!"})
        else:
            redis.set(user_login_lock_redis_key, 0)
            redis.expire(user_login_lock_redis_key, 600)

        user_info = User.query.filter_by(user_name=user_name).first()
        if user_info is not None:
            if (user_info.type == 'local' and User.check_password(user_info, password)) or (
                    user_info.type == 'ldap' and
                    app.config['LDAP_CONFIG'].get('login') and
                    ldap.auth(user_name, password)):
                redis.delete(user_login_lock_redis_key)
                redis.set(token, json.dumps({"user_name": user_name}))
                user_info.login_time = datetime.datetime.now()
                db.session.commit()
                return json.dumps({"code": 200, "msg": "", "token": token, "display_name": user_info.display_name})
        else:
            if app.config['LDAP_CONFIG'].get('login') and ldap.auth(user_name, password):
                ldap_user_dn = "uid=" + user_name + "," + app.config["LDAP_CONFIG"].get('people_dn')
                ldap_info = ldap.search(ldap_user_dn, "(objectClass=posixAccount)", ["displayName", "mail"])
                display_name = ldap_info[0]['displayName'][0]
                mail = ldap_info[0]['mail'][0]
                db.session.add(
                    User(
                        user_name=user_name,
                        email=mail,
                        display_name=display_name,
                        type='ldap',
                        login_time=datetime.datetime.now()
                    )
                )
                redis.delete(user_login_lock_redis_key)
                redis.set(token, json.dumps({"user_name": user_name}))
                db.session.commit()
                return json.dumps({"code": 200, "msg": "", "token": token, "display_name": display_name})
        redis.set(user_login_lock_redis_key, int(redis.get(user_login_lock_redis_key)) + 1)
        redis.expire(user_login_lock_redis_key, 600)
        return json.dumps({"code": 406, "msg": "账户密码错误!"})
    except Exception as Error:
        logging.error(Error)
        return json.dumps({"code": 500, "msg": "网络错误!"})


@Manage.route('/logout', methods=["POST"])
def logout():
    """
    用户注销操作
    :return:
    """
    try:
        data = json.loads(request.get_data())
        if redis.exists(data["token"]):
            redis.delete(data["token"])
        return json.dumps({"code": 200, "msg": ""})
    except Exception as Error:
        logging.error(Error)
        return json.dumps({"code": 500, "msg": "网络错误!"})
