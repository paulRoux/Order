#!/usr/bin/ python
# -*- coding: utf-8 -*-
__author__ = 'mtianyan'
__date__ = '2018-11-27 16:02'
"""
            　┏┓　　　┏┓+ +
  　　　　　　　┏┛┻━━━┛┻┓ + +
  　　　　　　　┃　　　　　　　┃ 　
  　　　　　　　┃　　　━　　　┃ ++ + + +
  　　　　　　 ████━████ ┃+
  　　　　　　　┃　　　　　　　┃ +
  　　　　　　　┃　　　┻　　　┃
  　　　　　　　┃　　　　　　　┃ + +
  　　　　　　　┗━┓　　　┏━┛
  　　　　　　　　　┃　　　┃　　　　　　　　　　　
  　　　　　　　　　┃　　　┃ + + + +
  　　　　　　　　　┃　　　┃　　　　Code is far away from bug with the animal protecting　　　　　　　
  　　　　　　　　　┃　　　┃ + 　　　　神兽保佑,代码无bug　　
  　　　　　　　　　┃　　　┃
  　　　　　　　　　┃　　　┃　　+　　　　　　　　　
  　　　　　　　　　┃　 　　┗━━━┓ + +
  　　　　　　　　　┃ 　　　　　　　┣┓
  　　　　　　　　　┃ 　　　　　　　┏┛
  　　　　　　　　　┗┓┓┏━┳┓┏┛ + + + +
  　　　　　　　　　　┃┫┫　┃┫┫
  　　　　　　　　　　┗┻┛　┗┻┛+ + + +
"""

from flask import Blueprint

route_order = Blueprint("order_page", __name__)


@route_order.route('/')
def index():

    return 'order index page'


@route_order.route('/hello')
def hello():
    return 'order hello'
