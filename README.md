=============================
django-disposable-email-checker
=============================

.. image:: https://badge.fury.io/py/DisposableEmailChecker.png
    :target: https://badge.fury.io/py/DisposableEmailChecker

.. image:: https://travis-ci.org/aaronbassett/DisposableEmailChecker.png?branch=master
    :target: https://travis-ci.org/aaronbassett/DisposableEmailChecker

Django package to detect ~890 domains used by disposable email services

Documentation
-------------

The full documentation is at https://DisposableEmailChecker.readthedocs.org.

Quickstart
----------

First install the package from pypi

    pip install django-disposable-email-checker

then in your app's models file:

    from disposable_email_checker.fields import DisposableEmailField

    class MyModel(models.Model):
        email = DisposableEmailField()
