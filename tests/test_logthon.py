# test_logthon.py
# -*- coding: utf-8 -*-

"""Tests for `logthon` package"""

import io
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


if __name__ == '__main__':
    unittest.main()
