#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from django.test import TestCase
from django.core.exceptions import ValidationError
from disposable_email_checker import validators
from disposable_email_checker.emails import email_domain_loader


class TestDisposableEmailValidator(TestCase):

    def setUp(self):
        self.disposable_email = "fake.mcfakerston@{domain}".format(
            domain=random.choice(email_domain_loader())
        )
        self.not_a_disposable_email = "sergey.brin@google.com"

    def test_validator(self):
        self.assertRaises(ValidationError, validators.validate_disposable_email, self.disposable_email)
        validators.validate_disposable_email(self.not_a_disposable_email)
