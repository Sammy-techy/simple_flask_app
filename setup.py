#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
from setuptools import setup
setup(
    name='simple_flask_app',
    version='1.0',
    license='GNU General Public License v3',
    author='Sam',
    author_email='aduoluwaseun@yahoo.com',
    description='simple student forum flask app',
    packages=['simple_flask_app'],
    platforms='any',
    install_requires=[
        'flask',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
