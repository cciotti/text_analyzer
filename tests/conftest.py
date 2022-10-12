# coding=utf-8
__date__ = "29 September 2022"

import logging
from contextlib import contextmanager

import pytest

logger = logging.getLogger(__name__)


@contextmanager
def does_not_raise():
    yield


@pytest.fixture
def test_data():
    with open("tests/test_data.txt") as data:
        yield data.read()


@pytest.fixture
def bad_test_data():
    yield None
