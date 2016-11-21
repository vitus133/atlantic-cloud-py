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
    pl = 'platform'
    ii = 'imageid'
    if i is None:
        tsv=''.join([
        pl,'   \t',
        ii,
        ])
    else:
        tsv=''.join([
        i[pl],'   \t',
        i[ii],
        ])
    return tsv

print(image_as_tsv())
    
images=me.image.describe()['describe-imageresponse']['imagesset']

imagek=sorted(images, key=lambda k: images[k]['imageid'].lower())

for k in imagek:
    print(image_as_tsv(images[k]))
    
print(len(images))
