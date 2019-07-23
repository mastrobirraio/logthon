# test_logthon.py
# -*- coding: utf-8 -*-

from datetime import datetime

from logthon import logthon as ln


def compose_text_message(level, message):
    return ln.STD_FORMAT.format(
        timestamp=datetime.now(),
        level=level,
        message=message
    )


def compose_log(level, message):
    text_message = compose_text_message(level, message)
    return '{color}{message}{reset_format}'.format(
        color=ln.LOG_LEVELS[level],
        message=text_message,
        reset_format=ln.RESET_FORMAT
    )
