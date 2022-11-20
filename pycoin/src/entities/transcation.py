import time
from pycoin.wallet import Wallet

class Transaction:
    def __init__(self, from_addr, to_addr, amount, data, blocks, pending_txs):
        self.from_addr = from_addr
        self.to_addr = to_addr
        self.amount = int(amount)
        self.data = data
        self.timestamp = time.time()
        self.prev_tx = self.get_prev_tx(blocks, pending_txs)
        self.hash = self.hash()
    def get_prev_tx(self, blocks, pending_txs):
        wallet = Wallet(self.from_addr)
        wallet.get_txs(blocks, pending_txs)
        print(wallet.txs)
        return ""


    def hash(self):
        return ""

    def sign(self, priv_key):
        return True     
