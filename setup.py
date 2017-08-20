# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

from flask_dynamo_session import __about__ as about

from pipfile import api as pipfile

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license_file = f.read()

setup(
    name=about.__package_name__,
    version=about.__version__,
    description=about.__doc__,
    long_description=readme,
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 2.7'
    ],
    keywords='flask dynamo dynamodb flask-dynamo',
    author=about.__author__,
    author_email=about.__email__,
    url=about.__website__,
    license=about.__license__,
    packages=find_packages(exclude=('docs', 'scripts', 'tests')),
    install_requires=pipfile.load().data['default'].keys()
)
