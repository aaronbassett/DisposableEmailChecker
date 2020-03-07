============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
-----------

Report bugs at https://github.com/jheld/DisposableEmailChecker/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
--------

Look through the GitHub issues for bugs. Anything tagged with "bug"
is open to whoever wants to implement it.

Implement Features
------------------

Look through the GitHub issues for features. Anything tagged with "feature"
is open to whoever wants to implement it.

Write Documentation
-------------------

django-disposable-email-checker could always use more documentation, whether as part of the
official django-disposable-email-checker docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
---------------

The best way to send feedback is to file an issue at https://github.com/jheld/DisposableEmailChecker/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `DisposableEmailChecker` for local development.

1. Fork the `DisposableEmailChecker` repo on GitHub.
2. Clone your fork locally

    $ git clone git@github.com:your_name_here/DisposableEmailChecker.git

3. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper installed, this is how you set up your fork for local development

    $ mkvirtualenv DisposableEmailChecker
    $ cd DisposableEmailChecker/
    $ python setup.py develop

4. Create a branch for local development

    $ git checkout -b name-of-your-bugfix-or-feature

Now you can make your changes locally.

5. When you're done making changes, check that your changes pass flake8 and the
tests, including testing other Python versions with tox

    $ flake8 disposable_email_checker tests
    $ python setup.py test
    $ tox

To get flake8 and tox, just pip install them into your virtualenv.

6. Commit your changes and push your branch to GitHub

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. Of note, the documentation build is currently broken -- there are plans to fix this; we will also accept pull
   requests to fix this!
3. The pull request should work for Python 3.5, 3.6, 3.7, 3.8, and for PyPy3. Check
   https://travis-ci.org/jheld/DisposableEmailChecker/pull_requests
   and make sure that the tests pass for all supported Python versions.

Tips
----

To run a subset of tests

    $ python -m unittest tests.test_disposable_email_checker
