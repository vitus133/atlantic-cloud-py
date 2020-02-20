from keyrings.cryptfile.cryptfile import CryptFileKeyring

class KeyRing():
    '''
    Platfiorm independent secrets management for applications
    based on encrypted files
    '''
    def __init__(self, service: str, pairs: list, passcode=''):
        '''
        Keyring initialization
        Parameters:
        service: A string representing a topic
        pairs: A list of dicts containing username and description pairs.
            
            pairs = [
                {
                    'username': 'pub_key',
                    'description': 'API Public Key'
                }
            ]
            If password is empty, when trying to acquire it from keyring,
            it will be prompted to be entered via stdin
        passcode: A keyring passcode. If empty, passcode will be prompted.
        '''
        self.kr = CryptFileKeyring()
        self.secrets = {}
        if not service in self.secrets.keys():
            self.secrets[service] = {}
        if passcode != '':
            self.kr.keyring_key = passcode
        for item in pairs:
            key = item.get('username')
            assert(key != None)
            password = self.kr.get_password(service, key)
            if not password:
                desc = item.get('description')
                if not desc:
                    desc = key
                correct = False
                while not correct:
                    print(f"Enter {desc}:")
                    password = input()
                    print(password)
                    print("Is that ok [y/N]:")
                    if input() == 'y':
                        correct = True
                self.kr.set_password(service, key, password)
            self.secrets[service][key] = password

    def get_secrets(self, service: str) -> dict:
        return self.secrets.get(service)      



if __name__ == "__main__":
    pairs = [
                {
                    'username': 'pub_key',
                    'description': 'API Public Key'
                },
                                {
                    'username': 'priv_key',
                    'description': 'API Private Key'
                },

            ]
    kr = KeyRing("atlantic", pairs, "qaqwse")
    print(kr.get_secrets("atlantic"))


    