# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import flask_dynamo_session

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license_file = f.read()

setup(
    name='flask_dynamo_session',
    version=flask_dynamo_session.__version__,
    description='Flask extension for storing session in dynamodb. Uses flask_dynamo.',
    long_description=readme,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha', 'Environment :: Console', 'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License', 'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.6'
    ],
    keywords='flask dynamo dynamodb, flask-dynamo',
    author='Austin Page',
    author_email='jaustinpage@gmail.com',
    url='https://github.com/jaustinpage/flask-dynamo-session',
    license=license_file,
    packages=find_packages(exclude=('docs', 'scripts', 'tests')))
