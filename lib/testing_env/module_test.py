#!/usr/bin/env python3
from versions import (
    python_version,
    requests_version,
    pytest_version
)

def test_python_version():
    version_info = python_version()
    assert version_info.major == 3
    assert version_info.minor == 8

def test_requests_version():
    assert requests_version() == "2.27.1"

def test_pytest_version():
    assert pytest_version() == "7.1.3"


# CodeGrade naming hook — must be last & properly formatted
def pytest_itemcollected(item):
    par = item.parent.obj
    node = item.obj
    pref = par.__doc__.strip() if par.__doc__ else par.__class__.__name__
    suf = node.__doc__.strip() if node.__doc__ else node.__name__
    if pref or suf:
        item._nodeid = ' '.join((pref, suf))
