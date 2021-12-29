import json
from eth_typing import HexStr
from web3 import Web3


class SmartContractService(object):
    def __init__(self):
        self.ganache_url = "http://127.0.0.1:7545"
        self.web3 = Web3(Web3.HTTPProvider(self.ganache_url))
        self.integrator_address = "0xEc0c8e81BDaB00a4A11D8955Ba7Aac69A29D98aa"
        self.account = self.web3.eth.accounts[0]

    @staticmethod
    def _read_smart_contract_file():
        # brownie init & brownie compile
        with open(
                "/home/recep/PycharmProjects/marketplace-eth-integrator/product/contracts/build/contracts/createProduct.json") as file:
            contract = json.load(file)
        return contract

    @property
    def _abi(self):
        return self._read_smart_contract_file()['abi']

    @property
    def _bytecode(self):
        return self._read_smart_contract_file()['bytecode']

    def write_to_eth(self, product_id: str, product_name: str, category: str,
                     price: int,
                     description: str) -> HexStr:
        product = self.web3.eth.contract(abi=self._abi,
                                         address=self.integrator_address,
                                         bytecode=self._bytecode)

        result = product.functions.addProduct(product_id, product_name,
                                              category,
                                              price,
                                              description).transact(
            {"From": self.account})
        return self.web3.toHex(result)

    def read_from_contract(self, tx):
        return self.web3.eth.waitForTransactionReceipt(tx)
