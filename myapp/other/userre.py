import re


class usernameRe():
    """检测用户名是否规范"""

    def __init__(self, username):
        self.username = username
        self.usr_re = "^[a-zA-z][a-zA-Z0-9_]{2,9}$"

    def isre(self):
        pattern = re.compile(self.usr_re)
        return re.match(pattern, self.username)


class emailRe():
    '''检测email'''

    def __init__(self, email):
        self.email = email
        self.ema_re = "^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$"

    def isre(self):
        pattern = re.compile(self.ema_re)
        return pattern.match(self.email)
