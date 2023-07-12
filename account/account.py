from web3 import Web3


class CreateAccount:
    def __init__(self, provider=None):
        self.w3 = Web3(Web3.HTTPProvider(provider or
                                         'https://mainnet.infura.io/'))

    def _check_connection(self):
        return self.w3.isConnected()

    def create(self, encrypt: str):
        try:
            if self._check_connection():
                account = self.w3.eth.account.create()
                return {
                    "Address": account.address,
                    "Private Key": self.w3.toHex(account.privateKey),
                    "Key Store": account.encrypt(encrypt)
                }
        except Exception as e:
            raise e
