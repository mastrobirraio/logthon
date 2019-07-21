# logthon.py
# -*- coding: utf-8 -*-

from datetime import datetime


"""
OUTPUT FORMAT
"""
STD_FORMAT = '[{timestamp}] {user} - {level}: {message}'

"""
COLORS
"""
YELLOW_FORMAT = '1;33;40m'
GREY_FORMAT = '1;30;40m'
RED_FORMAT = '1;31;40m'
GREEN_FORMAT = '1;32;40m'

"""
LEVELS
"""
INFO_LEVEL = 'INFO'
WARN_LEVEL = 'WARNING'
ERRO_LEVEL = 'ERROR'
SUCC_LEVEL = 'SUCCESS'


class Logthon:
    def __init__(self, user=None):
        self.format = STD_FORMAT
        if user:
            self.user = user
        else:
            self.user = 'unlogged'

    def set_user(self, user):
        self.user = user

    def compose_message(self, level, message):
        return self.format.format(
            timestamp=datetime.now(),
            user=self.user,
            level=level,
            message=message)

    def compose_output(self, color, message):
        return '\033[{}{}\033[00m'.format(color, message)

    def info(self, message):
        message = self.compose_message(INFO_LEVEL, message)
        print(self.compose_output(GREY_FORMAT, message))

    def warn(self, message):
        message = self.compose_message(WARN_LEVEL, message)
        print(self.compose_output(YELLOW_FORMAT, message))

    def error(self, message):
        message = self.compose_message(ERRO_LEVEL, message)
        print(self.compose_output(RED_FORMAT, message))
    
    def success(self, message):
        message = self.compose_message(SUCC_LEVEL, message)
        print(self.compose_output(GREEN_FORMAT, message))

