# -*- coding: utf-8 -*-
from flask_dynamo_session import __version__


def test_version():
    assert __version__.__version__ == "0.0.2"
