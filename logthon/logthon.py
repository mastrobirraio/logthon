# logthon.py
# -*- coding: utf-8 -*-

"""
Logthhon
~~~~~~~~

Loghton is a simple logger for Python
"""

from datetime import datetime

from colorama import Fore

"""OUTPUT FORMAT"""
STD_FORMAT = '[{timestamp}] - {level}: {message}'

"""COLORS"""
YELLOW_FORMAT = Fore.YELLOW
RED_FORMAT = Fore.RED
GREEN_FORMAT = Fore.GREEN
RESET_FORMAT = Fore.RESET

"""LEVELS"""
INFO_LEVEL = 'INFO'
WARN_LEVEL = 'WARNING'
ERRO_LEVEL = 'ERROR'
SUCC_LEVEL = 'SUCCESS'

"""LOG LEVELS"""
LOG_LEVELS = {
    INFO_LEVEL: RESET_FORMAT,
    WARN_LEVEL: YELLOW_FORMAT,
    ERRO_LEVEL: RED_FORMAT,
    SUCC_LEVEL: GREEN_FORMAT
}


class Logthon:

    def __init__(self):
        """Set the format global variable as class attribute"""
        self.format = STD_FORMAT

    def compose_message(self, level, message):
        """Compose the text message

        :param level: the log level one of the defined global LEVELS
        :param message: the message to log
        :return: the formatted string
        """
        return self.format.format(
            timestamp=datetime.now(),
            level=level,
            message=message)

    def compose_output(self, color, message):
        """Compose the output message

        :param color: the string color according to log level
        :param message: the message to log
        :return:
        """
        return '{}{}{}'.format(color, message, RESET_FORMAT)

    def info(self, message):
        """Print a log using INFO_LEVEL

        :param message: the message to log
        """
        message = self.compose_message(INFO_LEVEL, message)
        print(self.compose_output(LOG_LEVELS[INFO_LEVEL], message))

    def warn(self, message):
        """Print a log using WARN_LEVEL

        :param message: the message to log
        """
        message = self.compose_message(WARN_LEVEL, message)
        print(self.compose_output(LOG_LEVELS[WARN_LEVEL], message))

    def error(self, message):
        """Print a log using ERRO_LEVEL

        :param message: the message to log
        """
        message = self.compose_message(ERRO_LEVEL, message)
        print(self.compose_output(LOG_LEVELS[ERRO_LEVEL], message))
    
    def success(self, message):
        """Print a log using SUCC_LEVEL

        :param message: the message to log
        """
        message = self.compose_message(SUCC_LEVEL, message)
        print(self.compose_output(LOG_LEVELS[SUCC_LEVEL], message))
