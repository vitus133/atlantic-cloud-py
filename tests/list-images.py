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

def image_as_tsv(i=None):
    i1 = 'platform'
    i2 = 'architecture'
    i3 = 'imageid'

    if i is None:
        tsv=''.join([
        i1,'   \t',
        i2[:4],'\t',
        i3,
        ])
    else:
        tsv = ''.join([ 
        i[i1],'   \t',
        i[i2],'\t',
        i[i3],
        ])
    return tsv

print(image_as_tsv())
    
images=me.image.describe()['describe-imageresponse']['imagesset']

imagek=sorted(images, key=lambda k: images[k]['imageid'].lower())

for k in imagek:
    print(image_as_tsv(images[k]))
    
print(len(images))
