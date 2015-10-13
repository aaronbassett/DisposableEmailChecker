#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import disposable_email_checker

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = disposable_email_checker.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

if sys.argv[-1] == 'tag':
    print("Tagging the version on github:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-disposable-email-checker',
    version=version,
    description="""Django package to detect ~890 domains used by disposable email services""",
    long_description=readme + '\n\n' + history,
    author='Aaron Bassett',
    author_email='aaron@rawtech.io',
    url='https://github.com/aaronbassett/DisposableEmailChecker',
    packages=[
        'disposable_email_checker',
    ],
    include_package_data=True,
    install_requires=[
        'six'
    ],
    license="BSD",
    zip_safe=False,
    keywords='DisposableEmailChecker',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
