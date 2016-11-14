# Atlantic.net Cloud API Python Bindings

Atlantic.net API is described there:
https://www.atlantic.net/docs/api/

## Install
pip install . --user
or
sudo pip install .
or
pip install [-e] git+https://git.repo/some_pkg.git#egg=atlantic_python --user

For the last case options please see:
https://pip.pypa.io/en/latest/reference/pip_install/#vcs-support

## Example

```python
#!/usr/bin/python2
import atlantic as api
apiPubkey='ATL9876543210abcdef01234567890abcde'
apiPrivkey='9876543210abcdef01234567890abcde12345678'
me=api.Atlantic(apiPubkey,apiPrivkey)
i1='list-instancesresponse'
i2='instancesSet'
vId  ='InstanceId'
vSt  ='vm_status'
vIP  ='vm_ip_address'
il = me.server.list()[i1][i2]
h=''.join([vId,' ',          vSt,' ',     vIP  ])
print(h)
for k,v in il.items():
    d=''.join([v[vId],'      ',v[vSt],'   ',v[vIP] ])
    print(d)
```
## BUGS

This code is not compatible with Python 3
```
  File "/home/mz0/.local/lib/python3.5/site-packages/atlantic/utils.py", line 36, in _generate_signature
    sig = hmac.new(key=self.private_key, msg=string_to_sign, digestmod=hashlib.sha256)
  File "/usr/lib64/python3.5/hmac.py", line 144, in new
    return HMAC(key, msg, digestmod)
  File "/usr/lib64/python3.5/hmac.py", line 42, in __init__
    raise TypeError("key: expected bytes or bytearray, but got %r" % type(key).__name__)
```
## License

This code is provided under an MIT-style license. Please refer to the LICENSE
file in the root of the project for specifics.
