Atlantic.net Cloud API in Python
================================

Atlantic.net Cloud `API description
<https://www.atlantic.net/docs/api/>`_

Install
-------

::

    git clone https://github.com/mz0/atlantic-py.git py-api && cd py-api
    pip install . --user
    # or
    pip3 install . --user
    # or
    sudo pip install .
    # or omit cloning
    pip install git+https://github.com/mz0/atlantic-py.git --user


Example
-------

Please see `tests/manual.py`_. This module was checked with these commands:

::

    python  manual.py ~/atlantic-api.key
    python3 manual.py ~/atlantic-api.key

Bugs
----

- this code has no tests. Live-tested on Fedora 24 and Ubuntu 16.10 in Python 2.7/3.5
- this API hides choice of JSON/XML response format Atlantic.net offers

License
-------

This code is provided under an MIT-style license.
Please refer to the LICENSE file for specifics.

.. _`tests/manual.py`: https://github.com/mz0/atlantic-py/blob/master/tests/manual.py
