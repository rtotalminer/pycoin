class Transaction:
    def __init__(self, from_addr, to_addr, amount, data):
        self.from_addr = from_addr
        self.to_addr = to_addr
        self.amount = amount
        self.data = data
    def sign(self, priv_key):
        return True      