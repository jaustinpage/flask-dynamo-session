# -*- coding: utf-8 -*-
from flask_dynamo_session import __about__ as about


def test_about_version():
    assert about.__version__ == "0.0.3"
