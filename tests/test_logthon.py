# test_logthon.py
# -*- coding: utf-8 -*-

"""Tests for `logthon` package"""

from freezegun import freeze_time

from logthon import logthon as ln
from tests.utils import compose_log

Logthon = ln.Logthon()
FREEZE_DATE = '2012-01-14'


@freeze_time(FREEZE_DATE)
def test_info_level(capsys):
    message = 'This is an info test log'
    Logthon.info(message)
    captured = capsys.readouterr()
    assert compose_log(ln.INFO_LEVEL, message) in captured.out


@freeze_time(FREEZE_DATE)
def test_warn_level(capsys):
    message = 'This is a warn test log'
    Logthon.warn(message)
    captured = capsys.readouterr()
    assert compose_log(ln.WARN_LEVEL, message) in captured.out


@freeze_time(FREEZE_DATE)
def test_error_level(capsys):
    message = 'This is an error test log'
    Logthon.error(message)
    captured = capsys.readouterr()
    assert compose_log(ln.ERRO_LEVEL, message) in captured.out


@freeze_time(FREEZE_DATE)
def test_success_level(capsys):
    message = 'This is a success test log'
    Logthon.success(message)
    captured = capsys.readouterr()
    assert compose_log(ln.SUCC_LEVEL, message) in captured.out


@freeze_time(FREEZE_DATE)
def test_critical_level(capsys):
    message = 'This is a critical test log'
    Logthon.critical(message)
    captured = capsys.readouterr()
    assert compose_log(ln.CRITICAL_LEVEL, message) in captured.out


@freeze_time(FREEZE_DATE)
def test_debug_level(capsys):
    message = 'This is a debug test log'
    Logthon.debug(message)
    captured = capsys.readouterr()
    assert compose_log(ln.DEBUG_LEVEL, message) in captured.out
