# test_logthon.py
# -*- coding: utf-8 -*-

"""Tests for `logthon` package"""

import io
import os
import unittest.mock

from freezegun import freeze_time

from logthon.logthon import Logthon

FREEZE_DATE = '2012-01-14'


class TestLogthon(unittest.TestCase):

    def setUp(self):
        self.logthon = Logthon()

    @freeze_time(FREEZE_DATE)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_info_level(self, mock_stdout):
        message = 'This is an info test log'
        self.logthon.info(message)
        self.assertIn(message, mock_stdout.getvalue())

    @freeze_time(FREEZE_DATE)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_warn_level(self, mock_stdout):
        message = 'This is a warn test log'
        self.logthon.warn(message)
        self.assertIn(message, mock_stdout.getvalue())

    @freeze_time(FREEZE_DATE)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_error_level(self, mock_stdout):
        message = 'This is an error test log'
        self.logthon.error(message)
        self.assertIn(message, mock_stdout.getvalue())

    @freeze_time(FREEZE_DATE)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_critical_level(self, mock_stdout):
        message = 'This is a critical test log'
        self.logthon.critical(message)
        self.assertIn(message, mock_stdout.getvalue())

    @freeze_time(FREEZE_DATE)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_debug_level(self, mock_stdout):
        message = 'This is a debug test log'
        self.logthon.debug(message)
        self.assertIn(message, mock_stdout.getvalue())

    @freeze_time(FREEZE_DATE)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_success_level(self, mock_stdout):
        message = 'This is a success test log'
        self.logthon.warn(message)
        self.assertIn(message, mock_stdout.getvalue())


class TestLogthonDefaultFile(unittest.TestCase):

    def setUp(self):
        self.temp_file = '../logthon/logthon.log'
        self.logthon = Logthon(save_log=True)

    def _clean(self):
        os.remove(self.temp_file)

    @freeze_time(FREEZE_DATE)
    def test_info_level(self):
        message = 'This is an info test log'
        self.logthon.info(message)
        with open(self.temp_file) as log_file:
            self.assertIn(message, log_file.read())
        self._clean()

    @freeze_time(FREEZE_DATE)
    def test_warn_level(self):
        message = 'This is a warn test log'
        self.logthon.warn(message)
        with open(self.temp_file) as log_file:
            self.assertIn(message, log_file.read())
        self._clean()

    @freeze_time(FREEZE_DATE)
    def test_error_level(self):
        message = 'This is an error test log'
        self.logthon.error(message)
        with open(self.temp_file) as log_file:
            self.assertIn(message, log_file.read())
        self._clean()

    @freeze_time(FREEZE_DATE)
    def test_critical_level(self):
        message = 'This is a critical test log'
        self.logthon.critical(message)
        with open(self.temp_file) as log_file:
            self.assertIn(message, log_file.read())
        self._clean()

    @freeze_time(FREEZE_DATE)
    def test_debug_level(self):
        message = 'This is a debug test log'
        self.logthon.debug(message)
        with open(self.temp_file) as log_file:
            self.assertIn(message, log_file.read())
        self._clean()

    @freeze_time(FREEZE_DATE)
    def test_success_level(self):
        message = 'This is a success test log'
        self.logthon.success(message)
        with open(self.temp_file) as log_file:
            self.assertIn(message, log_file.read())
        self._clean()


class TestLogthonCustomFile(TestLogthonDefaultFile):

    def setUp(self):
        self.file_name = 'app.log'
        self.temp_file = '../logthon/{}'.format(self.file_name)
        self.logthon = Logthon(save_log=True, filename=self.file_name)

    @freeze_time(FREEZE_DATE)
    def test_info_level(self):
        super(TestLogthonCustomFile, self).test_info_level()
    
    @freeze_time(FREEZE_DATE)
    def test_warn_level(self):
        super(TestLogthonCustomFile, self).test_warn_level()
        
    @freeze_time(FREEZE_DATE)
    def test_error_level(self):
        super(TestLogthonCustomFile, self).test_error_level()

    @freeze_time(FREEZE_DATE)
    def test_critical_level(self):
        super(TestLogthonCustomFile, self).test_critical_level()
    
    @freeze_time(FREEZE_DATE)
    def test_debug_level(self):
        super(TestLogthonCustomFile, self).test_debug_level()
    
    @freeze_time(FREEZE_DATE)
    def test_success_level(self):
        super(TestLogthonCustomFile, self).test_success_level()


class TestLogthonWithModule(TestLogthon):

    def setUp(self):
        self.logthon = Logthon(module_name=__name__)

    @freeze_time(FREEZE_DATE)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_info_level(self, mock_stdout):
        message = 'This is an info test log'
        self.logthon.info(message)
        self.assertIn(message, mock_stdout.getvalue())

    @freeze_time(FREEZE_DATE)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_warn_level(self, mock_stdout):
        message = 'This is a warn test log'
        self.logthon.warn(message)
        self.assertIn(message, mock_stdout.getvalue())

    @freeze_time(FREEZE_DATE)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_error_level(self, mock_stdout):
        message = 'This is an error test log'
        self.logthon.error(message)
        self.assertIn(message, mock_stdout.getvalue())

    @freeze_time(FREEZE_DATE)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_critical_level(self, mock_stdout):
        message = 'This is a critical test log'
        self.logthon.critical(message)
        self.assertIn(message, mock_stdout.getvalue())

    @freeze_time(FREEZE_DATE)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_debug_level(self, mock_stdout):
        message = 'This is a debug test log'
        self.logthon.debug(message)
        self.assertIn(message, mock_stdout.getvalue())

    @freeze_time(FREEZE_DATE)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_success_level(self, mock_stdout):
        message = 'This is a success test log'
        self.logthon.warn(message)
        self.assertIn(message, mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
