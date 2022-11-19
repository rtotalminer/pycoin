from flask import Flask
from flask import render_template
import json
from flask import jsonify
from flask import request
from pycoin.blockchain import Blockchain
from pycoin.blockchain import Transaction
from pycoin.crypto import model


app = Flask(__name__)

b = Blockchain()

@app.get("/blockchain")
def blockchain():
    blockchain_model = json.loads(json.dumps(b, indent=4, cls=model))
    return jsonify(blockchain_model)

@app.route("/mine")
def mine():
    miner_address = request.args.get('miner_address', None)
    b.mine_block(miner_address)
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

    b.validate_tx(tx)
    b.pending_txs.append(tx)

    tx_model = json.loads(json.dumps(tx, indent=4, cls=model))
    return tx_model