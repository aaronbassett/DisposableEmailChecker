#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import disposable_email_checker

from setuptools import setup

version = disposable_email_checker.__version__

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    os.system("python setup.py bdist_wheel upload")
    sys.exit()

if sys.argv[-1] == "tag":
    print("Tagging the version on github:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

readme = open("README.md").read()

setup(
    name="django-disposable-email-checker",
    version=version,
    description="""Django package to detect ~890 domains used by disposable email services""",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Jason Held",
    author_email="jasonsheld@gmail.com",
    url="https://github.com/jheld/DisposableEmailChecker",
    packages=["disposable_email_checker",],
    include_package_data=True,
    install_requires=["block-disposable-email>=2.0.0",],
    license="BSD",
    zip_safe=False,
    keywords="DisposableEmailChecker",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
