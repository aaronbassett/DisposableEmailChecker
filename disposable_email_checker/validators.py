# -*- coding: utf-8 -*-

import re
from six.moves import range
from django.conf import settings
from django.utils.encoding import force_text
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .emails import email_domain_loader


class DisposableEmailChecker():
    """
    Check if an email is from a disposable email service
    """

    message = _('Blocked email provider.')
    code = 'invalid'
    whitelist = []

    def __init__(self, message=None, code=None, whitelist=None):
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code
        if whitelist is not None:
            self.whitelist = whitelist

        self.emails = self._load_emails()

    def __call__(self, value):
        value = force_text(value)
        user_part, domain_part = value.rsplit('@', 1)

        if domain_part not in self.whitelist:
            for email_group in self.chunk(self.emails, 20):
                regex = "(.*" + "$)|(.*".join(email_group) + "$)"
                if re.match(regex, value):
                    raise ValidationError(self.message, code=self.code)

    def _load_emails(self):
        return getattr(
            settings, "DISPOSABLE_EMAIL_DOMAINS_LOADER", email_domain_loader
        )()

    def chunk(self, l, n):
        return (l[i:i+n] for i in range(0, len(l), n))

validate_disposable_email = DisposableEmailChecker()
