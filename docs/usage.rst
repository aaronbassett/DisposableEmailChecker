========
Usage
========

To use django-disposable-email-checker in a project::

    from disposable_email_checker.fields import DisposableEmailField

    class MyModel(models.Model):
        email = DisposableEmailField()
