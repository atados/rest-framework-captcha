======================
Django Rest Framework Captcha
======================

.. image:: https://img.shields.io/codeship/7710f3b0-1d5b-0135-3aa1-76e9fcc9c81a/master.svg?style=flat-square
  :target: https://img.shields.io/codeship/7710f3b0-1d5b-0135-3aa1-76e9fcc9c81a/master.svg?style=flat-square
.. image:: https://img.shields.io/codecov/c/github/leonardoarroyo/rest-framework-captcha.svg?style=flat-square
  :target: https://codecov.io/gh/leonardoarroyo/rest-framework-captcha
.. image:: https://readthedocs.org/projects/rest-framework-captcha/badge/?version=stable&style=flat-square
  :target: https://rest-framework-captcha.readthedocs.io/en/stable/
.. image:: https://img.shields.io/pypi/v/rest-framework-captcha.svg?style=flat-square
  :target: https://pypi.python.org/pypi/rest-framework-captcha/

Address model backed by Google Maps API for your project.

Getting Started
---------------
Installing
""""""""""""""
1. Install rest-framework-captcha::

    pip install rest-framework-catpcha

2. Add it to `INSTALLED_APPS` on `settings.py`::

    INSTALLED_APPS = [
      ...,
      'rest_framework_captcha'
    ]

3. Migrate::
  
    ./manage.py migrate


Using
""""""""""""""


Documentation
---------------

You can check the complete documentation `here <http://rest-framework-captcha.readthedocs.io/en/stable/>`_.

Testing
---------------
To test this module

::

  python rest_framework_captcha/tests/runtests.py

Versioning
---------------
We use `SemVer <http://semver.org/>`_ for versioning. For the versions available, see the `tags on this repository <https://github.com/leonardoarroyo/rest-framework-captcha/tags>`_. 

License
---------------
This project is licensed under the MIT License. See the `LICENSE.md <https://github.com/leonardoarroyo/rest-framework-captcha/blob/master/LICENSE.md>`_ file for details.
