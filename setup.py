from setuptools import setup, find_packages


setup(
    name = "django-disposable-email-checker",
    version = "0.1.2",
    packages = find_packages(),
    author = "Aaron Bassett",
    author_email = "me@aaronbassett.com",
    description = "Python class for use with Django to detect Disposable Emails",
    license = "MIT License",
    keywords = "django email disposable validation",
    url = "https://github.com/aaronbassett/DisposableEmailChecker",
    
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2 :: Only',
        'Framework :: Django'
    ]
)