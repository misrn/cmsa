# -*- coding: utf-8 -*-
import json
from ldap3 import Connection, Server, ALL, MODIFY_ADD, MODIFY_REPLACE, MODIFY_DELETE
from app import *


class Ldap:
    def __init__(self):
        self.ldap_server = Server(
            app.config["LDAP_CONFIG"].get('host'),
            get_info=ALL,
            connect_timeout=20
        )
        self.connection = Connection(
            self.ldap_server,
            user=app.config["LDAP_CONFIG"].get('user'),
            password=app.config["LDAP_CONFIG"].get('password'),
            auto_bind=True
        )

    def search(self, search_dn, search_filter, attributes):
        """
        Ldap 服务器数据查询接口
        :param search_dn:
        :param search_filter:
        :param attributes:
        :return:
        """
        self.connection.search(search_dn, search_filter, attributes=attributes)
        response = []
        for i in self.connection.entries:
            data = json.loads(i.entry_to_json())
            response.append(data["attributes"])
        self.connection.unbind()
        return response

    @staticmethod
    def auth(user_name, password):
        """
        Ldap 用户密码认证接口
        :param user_name:
        :param password:
        :return:
        """
        ldap_user_dn = "uid=" + user_name + "," + app.config["LDAP_CONFIG"].get('people_dn')
        ldap_server = Server(app.config["LDAP_CONFIG"].get('host'), get_info=ALL)
        ldap_connect = Connection(ldap_server, user=ldap_user_dn, password=password)
        return ldap_connect.bind()
