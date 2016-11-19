Atlantic.net Cloud API in Python
================================

Atlantic.net API is described there: https://www.atlantic.net/docs/api/

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
    pip install git+https://github.com/mz0/atlantic-py.git#egg=atlantic --user

For the last case options please see:
https://pip.pypa.io/en/latest/reference/pip\_install/#vcs-support

Example
-------

.. code:: python
    #!/usr/bin/python
    import atlantic as api

    apiPubkey=b'ATL9876543210abcdef01234567890abcde'
    apiPrivkey=b'9876543210abcdef01234567890abcde12345678'

    i1='list-instancesresponse'
    i2='instancesSet'
    vId  ='InstanceId'
    vSt  ='vm_status'
    vIP  ='vm_ip_address'

    me=api.Atlantic(apiPubkey,apiPrivkey)
    il = me.server.list()[i1][i2]

    h=''.join([    vId,' ',          vSt,' ',     vIP  ])
    print(h)

    for k,v in il.items():
        d=''.join([v[vId],'      ',v[vSt],'   ',v[vIP] ])
        print(d)

BUGS
----

This code has no test suite. Tested manually on Fedora 24 in Python 2.7/3.5
Also please note that items() use as above is suboptimal in Python 2.

License
-------

This code is provided under an MIT-style license. Please refer to the LICENSE
file in the root of the project for specifics.
