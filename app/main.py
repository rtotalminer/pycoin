from flask import Flask
from flask import render_template
import json
from flask import jsonify
from flask import request
from pycoin.blockchain import Blockchain
from pycoin.blockchain import Transaction
from pycoin.crypto import model
from pycoin.wallet import Wallet

from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)

b = Blockchain()

@app.get("/")
def main():
    return {"version": 1.0}

@app.get("/docs")
def docs():
    return render_template("index.html")

@app.get("/blockchain")
def blockchain():
    blockchain_model = json.loads(json.dumps(b, indent=4, cls=model))
    return jsonify(blockchain_model)

@app.route("/mine")
def mine():
    miner_address = request.args.get('miner_address', None)
    if not (b.mine_block(miner_address)):
        return "Invalid params"
    block = b.blocks[-1]
    block_model = json.loads(json.dumps(block, indent=4, cls=model))
    return jsonify(block_model)

@app.route("/tx")
def tx():
    from_addr = request.args.get('from_addr', None)
    to_addr = request.args.get('to_addr', None)
    amount = request.args.get('amount', None)
    data = request.args.get('data', None)
    priv_key = request.args.get('priv_key', None)

    tx = Transaction(from_addr, to_addr, amount, data)
    if not (tx.sign(priv_key)):
        return "Bad Request!"

    if not (b.validate_tx(tx)):
        return "Invalid transcation"
    

    tx_model = json.loads(json.dumps(tx, indent=4, cls=model))
    return tx_model

@app.route("/wallet")
def wallet():
    addr = request.args.get('addr', None)
    wallet = Wallet(addr)
    wallet.get_wallet_bal(b.blocks, b.pending_txs)
    wallet.get_txs(b.blocks, b.pending_txs)
    wallet_model = json.loads(json.dumps(wallet, indent=4, cls=model))
    return wallet_model
