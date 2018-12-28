#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
RESTful API for the EMC Common Event Enabler
"""
from setuptools import setup, find_packages


setup(name="vlab-cee-api",
      author="Nicholas Willhite,",
      author_email='willnx84@gmail.com',
      version='2018.12.22',
      packages=find_packages(),
      include_package_data=True,
      package_files={'vlab_cee_api' : ['app.ini']},
      description="RESTful API for the EMC Common Event Enabler",
      install_requires=['flask', 'ldap3', 'pyjwt', 'uwsgi', 'vlab-api-common',
                        'ujson', 'cryptography', 'vlab-inf-common', 'celery']
      )
