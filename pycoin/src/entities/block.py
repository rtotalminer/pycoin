import time

class Header:
    def __init__(self, index, seed, prev_hash):
        self.index = index
        self.seed = seed
        self.prev_hash = prev_hash
        self.time = time.time()

class Block:
    def __init__(self, index, seed, prev_hash, txs, root):
        self.header = Header(index, seed, prev_hash)
        self.txs = txs
        self.root = root

    