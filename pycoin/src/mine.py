
def mine(addr):
       
        if not (addr):
            return False

        difficulty = get_difficulty()
        reward = get_reward()
        coinbase_data = ["Coinbase"]

        if (len(self.blocks) == 0):
            prev_hash = "0x00"
        else: 
            prev_hash = hash_contents(self.blocks[-1])

        if (len(self.pending_txs) > 0):
            txs = self.pending_txs
        else:
            txs = []

        coinbase = Transaction(SU_ADDR, addr, reward, coinbase_data)
        txs.append(coinbase)

        tx_root = root_hash(txs)

        block = Block(txs, index, prev_hash, miner_address, tx_root)

        while not (hash_contents(block).startswith('0' * difficulty)):
            block.seed += 1

        self.blocks.append(block)
        self.curr_supply = self.get_current_supply()
        self.pending_txs = [] # remove txs

        return True
