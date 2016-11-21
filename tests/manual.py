import sys
import os
import atlantic as api

keyfile=os.path.expanduser(sys.argv[1])
key = {}
with open(keyfile) as kf:
    for line in kf:
        name, val = line.split()
        key[name.lower()]=val.encode()

me=api.Atlantic(key['public'],key['private'])

i1='list-instancesresponse'
i2='instancesSet'
il = me.server.list()[i1][i2]

vId  ='InstanceId'
vSt  ='vm_status'
vIP  ='vm_ip_address'

h=''.join([      vId,' ',        vSt,' ',     vIP  ])
print(h)

# warning: items() is suboptimal in Python 2
for k,v in il.items():
    d=''.join([v[vId],'      ',v[vSt],'   ',v[vIP] ])
    print(d)
