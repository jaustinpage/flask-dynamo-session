# -*- coding: utf-8 -*-

import os
import sys

sys.path.insert(0,
                os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import flask_dynamo_session  # noqa pylint: disable=wrong-import-position,unused-import
