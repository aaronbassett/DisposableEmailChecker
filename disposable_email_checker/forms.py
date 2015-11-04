# -*- coding: utf-8 -*-

from django import forms
from django.core import validators
from .validators import validate_disposable_email


class DisposableEmailField(forms.EmailField):
    default_validators = [validators.validate_email, validate_disposable_email]
