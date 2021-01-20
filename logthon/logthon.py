# logthon.py
# -*- coding: utf-8 -*-

"""
Logthon
~~~~~~~~

Loghton is a simple logger for Python
"""
from datetime import datetime
from sys import exit as sys_exit

from colorama import Fore

"""OUTPUT FORMAT"""
STD_FORMAT = '[{timestamp}] - {level}: {message}'
MODULE_FORMAT = '[{timestamp}] {module_name} - {level}: {message}'

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

    def __init__(self, save_log=False, filename='logthon.log', module_name=None):
        """Set the format global variable as class attribute"""
        self.__filename = filename
        self.__save_log = save_log
        self.__module_name = module_name
        self.__set_format()

    def __set_format(self):
        if self.__module_name is None:
            self._format = STD_FORMAT
        else:
            self._format = MODULE_FORMAT
            
    def __log_to_file(self, message):
        if self.__save_log:
            with open(self.__filename, 'a') as log_file:
                log_file.write(f'{message}\n')

    def __compose_message(self, level, message):
        """Compose the text message

        :param level: the log level one of the defined global LEVELS
        :param message: the message to log
        :return: the formatted string
        """
        if self._format == STD_FORMAT:
            log_message = self._format.format(
                timestamp=datetime.now(),
                level=level,
                message=message
            )
        else:
            log_message = self._format.format(
                timestamp=datetime.now(),
                level=level,
                message=message,
                module_name=self.__module_name
            )
        self.__log_to_file(log_message)
        return log_message

    def __compose_output(self, color, message):
        """Compose the output message

        :param color: the string color according to log level
        :param message: the message to log
        :return:
        """
        return f'{color}{message}{RESET_FORMAT}'

    def __level_exists(self, level):
        return level in LOG_LEVELS.keys()

    def info(self, message):
        """Print a log using INFO_LEVEL

        :param message: the message to log
        """
        message = self.__compose_message(INFO_LEVEL, message)
        print(self.__compose_output(LOG_LEVELS[INFO_LEVEL], message))

    def warn(self, message):
        """Print a log using WARN_LEVEL

        :param message: the message to log
        """
        message = self.__compose_message(WARN_LEVEL, message)
        print(self.__compose_output(LOG_LEVELS[WARN_LEVEL], message))

    def error(self, message):
        """Print a log using ERRO_LEVEL

        :param message: the message to log
        """
        message = self.__compose_message(ERRO_LEVEL, message)
        print(self.__compose_output(LOG_LEVELS[ERRO_LEVEL], message))
    
    def success(self, message):
        """Print a log using SUCC_LEVEL

        :param message: the message to log
        """
        message = self.__compose_message(SUCC_LEVEL, message)
        print(self.__compose_output(LOG_LEVELS[SUCC_LEVEL], message))

    def critical(self, message):
        """Print a log using CRITICAL_LEVEL

        :param message: the message to log
        """
        message = self.__compose_message(CRITICAL_LEVEL, message)
        print(self.__compose_output(LOG_LEVELS[CRITICAL_LEVEL], message))

    def debug(self, message):
        """Print a log using DEBUG_LEVEL

        :param message: the message to log
        """
        message = self.__compose_message(DEBUG_LEVEL, message)
        print(self.__compose_output(LOG_LEVELS[DEBUG_LEVEL], message))

    def log_and_exit_with_code(self, message, level=CRITICAL_LEVEL, error_code=1):
        """Print a log using level defined by user and exit program with error code defined by user

        :param message: the message to log
        :param level: the level to use to log message
        :param error_code: the code to use when exit
        """
        if self.__level_exists(level):
            message = self.__compose_message(level, message)
            print(self.__compose_output(LOG_LEVELS[level], message))
            sys_exit(error_code)
        self.critical('Log level doesn\'t exists')
        sys_exit(1)

    def pretty_print(self, message, dicts, level=DEBUG_LEVEL):
        """ Print a log with dictonioray or list prettifying the output. Default log level is DEBUG

        :param message: the message to log
        :param dicts: the dict to prettify
        :param level: the level to use to log message
        """

        import json

        if self.__level_exists(level):
            message = self.__compose_message(level, '{}: {}'.format(message, json.dumps(dicts, indent=4, default=str)))
            print(self.__compose_output(LOG_LEVELS[level], message))
        else:
            self.critical('Log level dosent\'t exists')

