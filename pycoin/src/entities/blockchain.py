from pycoin.block import Block
from pycoin.transcation import Transaction
from pycoin.crypto import hash_contents
from pycoin.merkle import root_hash, hash_map
from pycoin.wallet import Wallet


class Blockchain:
    def __init__(self):
        self.pending_txs = []
        self.blocks = []
        self.max_supply = 1e+5
        self.curr_supply = 1e+5
        #self.mine_block("0x1")

    def get_difficulty(self):
        return 1

    def validate_tx(self, tx):
        wallet = Wallet(tx.from_addr)
        bal = wallet.get_wallet_bal(self.blocks, self.pending_txs)
        print(bal)
        if (int(tx.amount) > bal):
            return False

        self.pending_txs.append(tx)
        return True

    def verify_blocks():
        pass
        # verify each block prev_tx matches
        # and seed matches


    def get_current_supply(self):
        current_supply = 0
        for block in self.blocks:
            for tx in block.txs:
                if tx.from_addr == "0x00":
                    current_supply += float(tx.amount)
        return self.max_supply - current_supply

    def mine_block(self, miner_address):

        difficulty = self.get_difficulty()
        amount = 10**(1/difficulty)

        if not (miner_address):
            return False

        if (len(self.blocks) == 0):
            prev_hash = "0x00"
        else: 
            prev_hash = hash_contents(self.blocks[-1])

        if (len(self.pending_txs) > 0):
            txs = self.pending_txs
        else:
            txs = []

        coinbase = Transaction("0x00", miner_address, int(amount), ["coinbase"], self.blocks, self.pending_txs)

        txs.append(coinbase)
        tx_root = root_hash(txs)

        block = Block(txs, len(self.blocks), prev_hash, miner_address, tx_root)

        while not (hash_contents(block).startswith('0' * difficulty)):
            block.seed += 1

        self.blocks.append(block)
        self.curr_supply = self.get_current_supply()
        self.pending_txs = [] # remove txs

        return True
