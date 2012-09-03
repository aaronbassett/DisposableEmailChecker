from setuptools import setup, find_packages


setup(
    name = "django-disposable-email-checker",
    version = "0.1",
    packages = find_packages(),
    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
    },
    author = "Aaron Bassett",
    author_email = "me@aaronbassett.com",
    description = "Python class for use with Django to detect Disposable Emails",
    license = "MIT",
    keywords = "django email disposable validation",
    url = "https://github.com/aaronbassett/DisposableEmailChecker",
)