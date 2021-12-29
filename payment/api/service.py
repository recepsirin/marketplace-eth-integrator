from web3 import Web3


class PaymentTransactionService(object):
    def __init__(self, gas_price="50"):
        self.ganache_url = "http://127.0.0.1:7545"
        self.web3 = Web3(Web3.HTTPProvider(self.ganache_url))
        self._gas_price = gas_price

    def _sign(self, transaction, private_key):
        return self.web3.eth.account.signTransaction(transaction,
                                                     private_key)

    def _get_nonce(self, _from):
        return self.web3.eth.getTransactionCount(_from)

    def send(self, _from, to, price, private_key):
        transaction = {
            "nonce": self._get_nonce(_from),
            "to": to,
            "value": self.web3.toWei(price, "ether"),
            "gas": 2000000,
            "gasPrice": self.web3.toWei(self._gas_price, "gwei")
        }
        signed = self._sign(transaction, private_key)
        return self.web3.toHex(
            self.web3.eth.sendRawTransaction(signed.rawTransaction))
