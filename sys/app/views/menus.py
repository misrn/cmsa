# -*- coding: utf-8 -*-
from flask import Blueprint
from app.views.common import *
from ldap3 import Connection, Server, ALL
import uuid
import json

Menu = Blueprint('menu', __name__)


@Menu.route('/list', methods=["POST"])
def lists():
    """
    菜单请求接口
    :return:
    """

    return json.dumps({"code": 200, "data": [
        {"cite": "系统管理",
         "icon": "&#xe6a9;",
         "second": [
             {
                 "uuid": "46707044-7c4f-4771-b509-7a01358e07aa",
                 "cite": "统计管理",
                 "url": "welcome1.html"
             },
             {
                 "uuid": "46707044-7c4f-4771-b509-7a01358e07ab",
                 "cite": "列表管理",
                 "url": "member-list.html"
             },
             {
                 "uuid": "46707044-7c4f-4771-b509-7a01358e07ac",
                 "cite": "动态列表",
                 "url": "member-list1.html"
             },
             {
                 "uuid": "46707044-7c4f-4771-b509-7a01358e07ad",
                 "cite": "会员冻结",
                 "url": "member-del.html"
             }
         ]},
        {"cite": "订单管理",
         "icon": "&#xe6b8;",
         "second": [
             {
                 "uuid": "46707044-7c4f-4771-b509-7a01358e07ae",
                 "cite": "订单统计",
                 "url": "order-list.html"
             },
             {
                 "uuid": "46707044-7c4f-4771-b509-7a01358e07af",
                 "cite": "订单恢复",
                 "url": "order-list1.html"
             }
         ]},
    ]})
