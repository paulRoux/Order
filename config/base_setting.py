# -*- coding: utf-8 -*-
SERVER_PORT = 5000
DEBUG = False
# SQLALCHEMY_ECHO = False

# windows无法使用export，linux可以直接注释掉，并且开启application.py的__init__的配置注释
SQLALCHEMY_ECHO = True
SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1/orders?charset=utf8mb4'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ENCODING = "utf8mb4"

AUTH_COOKIE_NAME = "orders"

SEO_TITLE = "订餐系统"

# 过滤url
IGNORE_URLS = [
    "^/user/login"
]

IGNORE_CHECK_LOGIN_URLS = [
    "^/static",
    "^/favicon.ico"
]

API_IGNORE_URLS = [
    "^/api"
]

# 分页
PAGE_SIZE = 10
PAGE_DISPLAY = 10

# 状态
STATUS_MAPPING = {
    "1": "正常",
    "0": "已删除"
}

MINA_APP = {
    'appid': 'xxxxxxxxxxxxxx换自己的',
    'app_secret': '008c006e5d961eef7626b980ad5b043b',
    # 'paykey': 'xxxxxxxxxxxxxx换自己的',
    # 'mch_id': 'xxxxxxxxxxxx换自己的',
    'callback_url': '/api/order/callback'
}

UPLOAD = {
    'ext': ['jpg', 'gif', 'bmp', 'jpeg', 'png'],
    'prefix_path': '/web/static/upload/',
    'prefix_url': '/static/upload/'
}

APP = {
    'domain': 'http://127.0.0.1:5000'
}

PAY_STATUS_MAPPING = {
    "1": "已支付",
    "-8": "待支付",
    "0": "已关闭"
}

PAY_STATUS_DISPLAY_MAPPING = {
    "0": "订单关闭",
    "1": "支付成功",
    "-8": "待支付",
    "-7": "待发货",
    "-6": "待确认",
    "-5": "待评价"
}
