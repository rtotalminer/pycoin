
class Wallet:
    def __init__(self, address, private_key=None):
        self.address = address
        self.private_key = private_key
        self.txs = []
        self.balance = 0

    def get_wallet_bal(self, blocks, pending_txs):
        bal = 0
        # history
        for block in blocks:
            for tx in block.txs:
                if (tx.to_addr != tx.from_addr):
                    if (tx.to_addr == self.address):
                        bal += int(tx.amount)
                    if (tx.from_addr == self.address):
                        bal -= int(tx.amount)
        # pendings
        for tx in pending_txs:
            if (tx.to_addr != tx.from_addr):
                if (tx.to_addr == self.address):
                    bal += int(tx.amount)
                if (tx.from_addr == self.address):
                    bal -= int(tx.amount)
        self.balance = bal
        return bal

    def get_txs(self, blocks, pending_txs):
        txs = []
        # history
        for block in blocks:
            for tx in block.txs:
                if (tx.to_addr != tx.from_addr):
                    if (tx.to_addr == self.address):
                        txs.append(tx)
                    if (tx.from_addr == self.address):
                        txs.append(tx)
        # pendings
        for tx in pending_txs:
            if (tx.to_addr != tx.from_addr):
                if (tx.to_addr == self.address):
                    txs.append(tx)
                if (tx.from_addr == self.address):
                    txs.append(tx)
        self.txs = txs
