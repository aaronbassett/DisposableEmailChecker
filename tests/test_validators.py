#!/usr/bin/env python
# -*- coding: utf-8 -*-
import importlib
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
        self.assertRaises(
            ValidationError,
            validators.validate_disposable_email,
            self.disposable_email,
        )
        validators.validate_disposable_email(self.not_a_disposable_email)

    def test_validator_messages(self):
        with self.assertRaisesMessage(
            ValidationError, "Blocked email provider."
        ):
            validators.validate_disposable_email(self.disposable_email)

        with self.settings(BDEA_MESSAGE="Test message"):
            # As the `BDEA_MESSAGE` gets calculated at run time
            # we need to reload the module that
            #  defines the message.
            importlib.reload(validators)
            with self.assertRaisesMessage(ValidationError, "Test message"):
                validators.validate_disposable_email(self.disposable_email)

        # We need to reload the module again to set
        # the default functionality back to normal.
        importlib.reload(validators)
