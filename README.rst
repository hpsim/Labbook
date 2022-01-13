========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |github-actions| |requires|
        |
    * - package
      - | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/Labbook/badge/?style=flat
    :target: https://Labbook.readthedocs.io/
    :alt: Documentation Status

.. |github-actions| image:: https://github.com/greole/Labbook/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/greole/Labbook/actions

.. |requires| image:: https://requires.io/github/greole/Labbook/requirements.svg?branch=main
    :alt: Requirements Status
    :target: https://requires.io/github/greole/Labbook/requirements/?branch=main

.. |commits-since| image:: https://img.shields.io/github/commits-since/greole/Labbook/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/greole/Labbook/compare/v0.0.0...main



.. end-badges

A labbook handler

* Free software: GNU Lesser General Public License v3 or later (LGPLv3+)

Installation
============

::

    pip install labbook

You can also install the in-development version with::

    pip install https://github.com/greole/Labbook/archive/main.zip


Documentation
=============


https://Labbook.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
