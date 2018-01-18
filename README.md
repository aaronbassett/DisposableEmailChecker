=============================
django-disposable-email-checker
=============================

[![PyPI version](https://badge.fury.io/py/django-disposable-email-checker.png)](https://pypi.python.org/pypi/django-disposable-email-checker/)
[![PyPI version](https://travis-ci.org/aaronbassett/DisposableEmailChecker.png?branch=master)](https://travis-ci.org/aaronbassett/DisposableEmailChecker)
[![Requirements Status](https://requires.io/github/aaronbassett/DisposableEmailChecker/requirements.svg?branch=master)](https://requires.io/github/aaronbassett/DisposableEmailChecker/requirements/?branch=master)

Django package to detect between ~890 & ~8,600 domains used by disposable email services.
You can validate any email against our internal list of ~890 domains used by
disposable email services. Optionally you can also check each domain against
the [Block-Disposable-Email.com](http://block-disposable-email.com) API,
covering ~8,600 domains.

Setup
-----

Install the disposable email checker from PyPI

    pip install django-disposable-email-checker

The disposable email checker comes with a list of ~890 emails. If you would like
to provide your own email list create a function which returns a list of domains
to block.

```python
from disposable_email_checker.emails import email_domain_loader

def custom_email_domain_loader():
    # Anyone still using AOL will be too much of a customer service burden
    return [
        "aol.com",
    ] + email_domain_loader()
```

Then add the complete path including function name to your settings

```python
DEC_LOADER = "my.package.custom_email_domain_loader"
```

If you would like to use the [BDE](http://block-disposable-email.com)
integration add your API key to your Django settings

```python
BDEA_APIKEY = "abcnotarealkey123"
```

optionally you can configure the BDE API timeout in seconds (default 5)

```python
BDEA_TIMEOUT = 2
```

A default error message can be set globally for the validation checking (this is optional and if 
left blank it will default to `_('Blocked email provider.')`):

```python
BDEA_MESSAGE = '<blocked email message>'
```

There are two modes for emailing matching to determine if the email is considered disposable:
* Ending with domain
* Exactly matching domain

For example consider the email address `fake.mcfakerston@edropmail.me` if ending with domain is 
chosen the `dropmail.me` domain will match the email address as it ends with `dropmail.me` and be
considered as a disposable email address. If the exactly matching domain is chosen `edropmail.me` 
does not equal `dropmain.me` and it will not be considered a disposable email address.

By default the option of ending with the domain is used.

To enable exact domain matching add the following to your Django settings:
```python
DEC_MATCHING = 'EXACT'
```

Adding to your models
---------------------

Once you have completed setup add the `DisposableEmailField` to your models.

```python
from disposable_email_checker.fields import DisposableEmailField

class MyModel(models.Model):
    email = DisposableEmailField()
```

The `DisposableEmailField` has a few optional arguments

* **whitelist** - A list of emails which will always be allowed. Defaults
to `[]`
* **message** - The error message used by ValidationError if validation
fails. Defaults to `_('Blocked email provider.')`
* **code** - The error code used by ValidationError if validation fails.
Defaults to "invalid".

Using the validator
-------------------

If you want to use the validator by itself

```python
from django.core.exceptions import ValidationError
from disposable_email_checker.validators import validate_disposable_email

try:
    validate_disposable_email(email)
except ValidationError:
    pass
```
