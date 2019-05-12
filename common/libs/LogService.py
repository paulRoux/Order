# -*- coding: utf-8 -*-
from flask import request, g
from application import app, db
import json
from common.libs.Helper import get_current_date
from common.models.log.AppAccessLog import AppAccessLog
from common.models.log.AppErrorLog import AppErrorLog


class LogService(object):
    @staticmethod
    def add_access_log():
        target = AppAccessLog()
        target.target_url = request.url
        target.referer_url = request.referrer
        target.ip = request.remote_addr
        target.query_params = json.dumps(request.values.to_dict())
        if 'current_user' in g and g.current_user is not None:
            target.uid = g.current_user.uid
        target.ua = request.headers.get("User-Agent")
        target.created_time = get_current_date()
        db.session.add(target)
        db.session.commit()
        return True

    @staticmethod
    def add_error_log(content):
        if 'favicon.ico' in request.url:
            return
        target = AppErrorLog()
        target.target_url = request.url
        target.referer_url = request.referrer
        target.query_params = json.dumps(request.values.to_dict())
        target.content = content
        target.created_time = get_current_date()
        db.session.add(target)
        db.session.commit()
        return True
