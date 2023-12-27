from flask import Flask, request, jsonify
from web3 import Web3, HTTPProvider
from web3.contract import Contract

app = Flask(__name__)

# Setup Web3 connection
web3 = Web3(HTTPProvider('http://127.0.0.1:8545'))  # Update with your Ethereum node address

# Contract ABI and Address
contract_abi = []  # Replace with your contract ABI
contract_address = '0x...'  # Replace with your contract address
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

@app.route('/issue-check', methods=['POST'])
def issue_check():
    data = request.get_json()
    # Interact with the blockchain to issue a check
    return jsonify({"message": "Check issued", "check_id": 123})  # Example response

@app.route('/review-check', methods=['POST'])
def review_check():
    data = request.get_json()
    check_id = data.get("check_id")
    action = data.get("action")  # 'accept' or 'reject'
    return jsonify({"message": "Check reviewed", "status": action})

@app.route('/revise-check', methods=['POST'])
def revise_check():
    data = request.get_json()
    check_id = data.get("check_id")
    new_amount = data.get("new_amount")
    new_notes = data.get("new_notes")
    return jsonify({"message": "Check revised", "check_id": check_id})

if __name__ == '__main__':
    app.run(debug=True)
