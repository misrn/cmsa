# -*- coding: utf-8 -*-
from . import Api


@Api.route('/ldap/user/list', methods=['GET'])
def ldap_user_list():
    return "ldap user list"


@Api.route('/ldap/user/add', methods=['GET'])
def ldap_user_add():
    return "ldap user add"
