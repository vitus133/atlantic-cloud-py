from .utils import AtlanticBase

class AtlanticImage(AtlanticBase):
    def __init__(self, access_key, private_key):
        AtlanticBase.__init__(self, access_key, private_key)

    def describe(self, imageid=None):
        """
        List available cloud images or describe a specific cloud image
        (e.g. ubuntu-14.04_64bit)

        Link: https://www.atlantic.net/docs/api/?shell#describe-image
        """
        params = {
            "Action": "describe-image"
        }
        if imageid:
            params.update({"imageid": imageid})
        return self.request(params)
