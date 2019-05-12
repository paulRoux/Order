# -*- coding: utf-8 -*-
import hashlib, requests, random, string, json
from application import app


class MemberService(object):

    @staticmethod
    def generate_auth_code(member_info=None):
        m = hashlib.md5()
        str = "%s-%s-%s" % (member_info.id, member_info.salt, member_info.status)
        m.update(str.encode("utf-8"))
        return m.hexdigest()

    @staticmethod
    def generate_salt(length=16):
        keylist = [random.choice((string.ascii_letters + string.digits)) for i in range(length)]
        return "".join(keylist)

    @staticmethod
    def get_wechat_open_id(code):
        """获取openid"""
        url = "https://api.weixin.qq.com/sns/jscode2session?appid={0}&secret={1}&js_code={2}&grant_type=authorization_code" \
            .format(app.config['MINA_APP']['appid'], app.config['MINA_APP']['app_secret'], code)
        r = requests.get(url)
        res = json.loads(r.text)
        print(res)
        openid = None
        if 'openid' in res:
            openid = res['openid']
        return openid
