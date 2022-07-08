from blockchain import Blockchain
from flask import request
from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

blockchain = Blockchain()


#mine a new block
@app.route("/mine_block", methods=["GET"])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block["proof"]
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash=blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    response = {
        "msg":"you mine the block", 
        "proof":block["proof"],
        "previous_hash":block["previous_hash"],
        "index":block["index"],
        "timestamp":block["timestamp"]
    }
    return jsonify(response), 200


#get the full blockchain
@app.route("/get_chain", methods=["GET"])
def get_blockchain():
    return jsonify({
        "chain":blockchain.chain,
        "length":len(blockchain.chain)
    })

@app.route("/valid_chain", methods=["POST"])
def valid_blockchain():
    return jsonify({"is_valid":blockchain.is_chain_valid(request.json["chain"])})


app.run(host="0.0.0.0", port=8888)

