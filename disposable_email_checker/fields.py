# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core import validators

from .validators import validate_disposable_email
from .forms import DisposableEmailField as DisposableEmailFormField


class DisposableEmailField(models.EmailField):
    default_validators = [validators.validate_email, validate_disposable_email]
    description = _("Not a disposable email address")

    def formfield(self, **kwargs):
        # As with CharField, this will cause email validation to be performed
        # twice.
        defaults = {
            "form_class": DisposableEmailFormField,
        }
        defaults.update(kwargs)
        return super(DisposableEmailField, self).formfield(**defaults)
