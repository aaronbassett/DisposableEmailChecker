from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

setup(
    name = "django-disposable-email-checker",
    version = "0.1.1",
    packages = find_packages(),
    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
    },
    author = "Aaron Bassett",
    author_email = "me@aaronbassett.com",
    description = "Python class for use with Django to detect Disposable Emails",
    long_description=readme,
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