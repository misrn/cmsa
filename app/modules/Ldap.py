# -*- coding: utf-8 -*-
import json
from ldap3 import Connection, Server, ALL
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

    def add(self, dn, _class, attributes):
        """
        LDAP 添加数据
        :param dn: 唯一DN
        :param _class: objectClass 对象列表
        :param attributes: json格式数据
        :return: 布尔值
        """
        try:
            self.connection.add(dn, _class, attributes)
            return True
        except Exception as Error:
            logging.error(Error)
            return False

    def delete(self, dn):
        """
        LDAP 删除数据
        :param dn: 唯一DN
        :return:
        """
        try:
            self.connection.delete(dn)
            return True
        except Exception as Error:
            logging.error(Error)
            return False

    def modify(self, dn, data):
        """
        LDAP 数据DN数据，可新增/删除/修改
        :param dn: 唯一DN
        :param data: json格式数据   {'host': [(MODIFY_DELETE, [host])]} ; MODIFY_DELETE/MODIFY_ADD/MODIFY_REPLACE
        :return:
        """
        try:
            self.connection.modify(dn, data)
            return True
        except Exception as Error:
            logging.error(Error)
            return False
