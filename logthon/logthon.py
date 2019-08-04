# logthon.py
# -*- coding: utf-8 -*-

"""
Logthon
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
MAGENTA_FORMAT = Fore.MAGENTA
LT_YELLOW_FORMAT = Fore.LIGHTYELLOW_EX
RESET_FORMAT = Fore.RESET

"""LEVELS"""
INFO_LEVEL = 'INFO'
WARN_LEVEL = 'WARNING'
ERRO_LEVEL = 'ERROR'
SUCC_LEVEL = 'SUCCESS'
CRITICAL_LEVEL = 'CRITICAL'
DEBUG_LEVEL = 'DEBUG'

"""LOG LEVELS"""
LOG_LEVELS = {
    INFO_LEVEL: RESET_FORMAT,
    WARN_LEVEL: YELLOW_FORMAT,
    ERRO_LEVEL: RED_FORMAT,
    SUCC_LEVEL: GREEN_FORMAT,
    CRITICAL_LEVEL: MAGENTA_FORMAT,
    DEBUG_LEVEL: LT_YELLOW_FORMAT
}


class Logthon:

    def __init__(self, save_log=False, filename='logthon.log'):
        """Set the format global variable as class attribute"""
        self._format = STD_FORMAT
        self._filename = filename
        self._save_log = save_log

    def _log_to_file(self, message):
        if self._save_log:
            with open(self._filename, 'a') as log_file:
                log_file.write('{}\n'.format(message))

    def _compose_message(self, level, message):
        """Compose the text message

        :param level: the log level one of the defined global LEVELS
        :param message: the message to log
        :return: the formatted string
        """
        log_message = self._format.format(
            timestamp=datetime.now(),
            level=level,
            message=message
        )
        self._log_to_file(log_message)
        return log_message

    def _compose_output(self, color, message):
        """Compose the output message

        :param color: the string color according to log level
        :param message: the message to log
        :return:
        """
        return '{color}{message}{reset_format}'.format(
            color=color,
            message=message,
            reset_format=RESET_FORMAT
        )

    def info(self, message):
        """Print a log using INFO_LEVEL

        :param message: the message to log
        """
        message = self._compose_message(INFO_LEVEL, message)
        print(self._compose_output(LOG_LEVELS[INFO_LEVEL], message))

    def warn(self, message):
        """Print a log using WARN_LEVEL

        :param message: the message to log
        """
        message = self._compose_message(WARN_LEVEL, message)
        print(self._compose_output(LOG_LEVELS[WARN_LEVEL], message))

    def error(self, message):
        """Print a log using ERRO_LEVEL

        :param message: the message to log
        """
        message = self._compose_message(ERRO_LEVEL, message)
        print(self._compose_output(LOG_LEVELS[ERRO_LEVEL], message))
    
    def success(self, message):
        """Print a log using SUCC_LEVEL

        :param message: the message to log
        """
        message = self._compose_message(SUCC_LEVEL, message)
        print(self._compose_output(LOG_LEVELS[SUCC_LEVEL], message))

    def critical(self, message):
        """Print a log using CRITICAL_LEVEL

        :param message: the message to log
        """
        message = self._compose_message(CRITICAL_LEVEL, message)
        print(self._compose_output(LOG_LEVELS[CRITICAL_LEVEL], message))

    def debug(self, message):
        """Print a log using DEBUG_LEVEL

        :param message: the message to log
        """
        message = self._compose_message(DEBUG_LEVEL, message)
        print(self._compose_output(LOG_LEVELS[DEBUG_LEVEL], message))
