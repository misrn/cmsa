# # -*- coding: utf-8 -*-
# from app import db
# import datetime
# from werkzeug.security import generate_password_hash, check_password_hash
#
# """
# db.Integer - 整形
# db.String(255)  - 字符串 ， 255 长度
# db.Text    - text
#
# primary_key=True - 主键
# nullable=False   - 字段是否为空， True 允许； False 不允许
#
# """
#
#
# class Role(db.Model):
#     __tablename__ = 'role'
#     id = db.Column(db.Integer(), primary_key=True)
#     name = db.Column(db.String(80))
#     create_time = db.Column(db.DateTime)  # 创建时间
#
#     def __init__(self, name):
#         self.name = name
#         self.create_time = datetime.datetime.now()
#
#
# # 用户表
# class User(db.Model):
#     __tablename__ = 'user'
#     id = db.Column(db.Integer(), primary_key=True)  # 用户ID
#     user_name = db.Column(db.String(80))  # 登录名
#     display_name = db.Column(db.String(80))  # 显示名称
#     email_address = db.Column(db.String(80))  # 邮箱地址
#     phone_number = db.Column(db.Integer())  # 电话号码
#     password = db.Column(db.String(255))  # 密码
#     type = db.Column(db.String(80))  # 账户类型 local , ldap
#     role_id = db.Column(db.Integer, db.ForeignKey('role.id'))  # 外键role id
#     role = db.relationship('Role', backref=db.backref('posts', lazy='dynamic'))
#     create_time = db.Column(db.DateTime)  # 创建时间
#     login_time = db.Column(db.DateTime)  # 最后一次登录时间
#     open_id = db.Column(db.String(255))  # 微信OPEN_ID
#
#     def __init__(self, user_name, email, display_name, type, password=None, role=None, login_time=None):
#         self.user_name = user_name
#         self.email_address = email
#         self.create_time = datetime.datetime.now()
#         self.role_id = 1
#         self.display_name = display_name
#         if role is None:
#             role = Role.query.filter_by(name="默认").first()
#         if password is not None:
#             self.password = generate_password_hash(password)
#         self.type = type
#         if login_time is not None:
#             self.login_time = login_time
#         self.role = role
#
#     def __repr__(self):
#         return self.user_name
#
#     def check_password(self, password):
#         return check_password_hash(self.password, password)
#
#
# class Menu(db.Model):
#     __tablename__ = 'menu'
#     id = db.Column(db.Integer(), primary_key=True)
#     name = db.Column(db.String(80))
#     icon = db.Column(db.String(80))  # 图标
#     level = db.Column(db.Integer)  # 菜单级别 (1 2)
#     html = db.Column(db.String(80))
#     function = db.Column(db.String(80))  # 功能对应函数
#     create_time = db.Column(db.DateTime)
#
#     def __init__(self, name, icon, html, function, level=None):
#         self.name = name
#         self.icon = icon
#         self.html = html
#         self.function = function
#         if level is None:
#             level = 2
#         self.level = level
#         self.create_time = datetime.datetime.now()
#
#
# class Authority(db.Model):
#     __tablename__ = 'authority'
#     id = db.Column(db.Integer(), primary_key=True)
#     role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
#     menu_id = db.Column(db.Integer, db.ForeignKey('menu.id'))
#     role = db.relationship('Role', backref=db.backref('role', lazy='dynamic'))
#     menu = db.relationship('Menu', backref=db.backref('menu', lazy='dynamic'))
#     create_time = db.Column(db.DateTime)
#
#     def __init__(self, role, menu):
#         self.role = role
#         self.menu = menu
#         self.create_time = datetime.datetime.now()
