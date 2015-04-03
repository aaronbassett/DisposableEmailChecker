from django.conf import settings
import re


class DisposableEmailChecker():
    """
    Check if an email is from a disposable
    email service
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DisposableEmailChecker, cls).__new__(cls, *args, **kwargs)
        return cls._instance
 
    def __init__(self, *args, **kwargs):
        """
        Constructor
        Use instances of the class like previously but make them
        share only one class-level emails attribute.
        @param refresh: equivalent to True for updating from file (e.g. file changed)
        """
        if not hasattr(DisposableEmailChecker, 'emails') or kwargs.get('refresh', False):
            DisposableEmailChecker.emails = [line.strip() for line in open(settings.DISPOSABLE_EMAIL_DOMAINS)]
    
    def chunk(self, l, n):
        return (l[i:i + n] for i in range(0, len(l), n))

    def is_disposable(self, email):
        for email_group in self.chunk(DisposableEmailChecker.emails, 32):
            regex = "(.*{0})".format(")|(.*".join(email_group))
            if re.match(regex, email):
                return True

        return False
