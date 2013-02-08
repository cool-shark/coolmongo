#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(name='CoolMongo',
    version='0.5',
    description='Simple MongoDB ORM with Live Database Switch Feature',
    long_description=open('README.rst').read(),
    author='Umut Aydin',
    author_email='umut.aydin@coolshark.com',
    packages=['coolmongo'],
    license='MIT',
    requires=[
        "pymongo"
    ],
)