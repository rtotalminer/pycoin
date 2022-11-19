import time

class Block:
    def __init__(self, txs, index, prev_hash, miner_addr, tx_root):
        self.seed = 0
        self.timestamp = time.time()
        self.txs = txs
        self.index = index
        self.prev_hash = prev_hash
        self.miner_addr = miner_addr
        self.tx_root = tx_root
