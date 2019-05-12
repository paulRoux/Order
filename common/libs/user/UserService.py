# -*- coding: utf-8 -*-
import hashlib
import base64
import random
import string


class UserService(object):
    """
    为用户Service的通用方法
    """

    @staticmethod
    def generate_auth_code(user_info=None):
        m = hashlib.md5()
        user_str = "%s-%s-%s-%s" % (user_info.uid, user_info.login_name, user_info.login_pwd, user_info.login_salt)
        m.update(user_str.encode("utf-8"))
        return m.hexdigest()

    @staticmethod
    def generate_password(pwd, salt):
        m = hashlib.md5()
        pwd_str = "%s-%s" % (base64.encodebytes(pwd.encode("utf-8")), salt)
        m.update(pwd_str.encode("utf-8"))
        return m.hexdigest()

    @staticmethod
    def generate_salt(length=16):
        key_list = [random.choice((string.ascii_letters + string.digits)) for i in range(length)]
        return "".join(key_list)


if __name__ == '__main__':
    print(UserService.generate_password("ty158917", "cF3JfH5FJfQ8B2Ba"))
