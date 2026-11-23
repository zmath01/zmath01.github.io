# blockchain-food-safety

Line-by-Line Explanation of Data Structures and Algorithms

The snippets form a single-process Flask example. Indent the method snippets under `class Blockchain:` and place the Flask app and routes after the class. The index route expects a `templates/index.html` file.

<!--more-->

## **Imports**
```python
import datetime
import hashlib
import json
from threading import Lock
from flask import Flask, jsonify, render_template
```

- **datetime**: Standard library for timestamp generation
- **hashlib**: Cryptographic hashing library (SHA-256)
- **json**: For serializing objects to JSON format
- **Lock**: Serializes access to the in-memory chain across request threads
- **Flask**: Web framework for creating REST API endpoints

---

## **Blockchain Class Definition**

### **Constructor**
```python
def __init__(self):
    self.chain = []
    self.create_block(proof=1, previous_hash='0')
```

- **Data Structure**: `self.chain` is a **list** that stores all blocks in the blockchain
- **Algorithm**: Genesis block creation - initializes the chain with the first block

---

### **create_block() Method**
```python
def create_block(self, proof, previous_hash):
    block = {
        'index': len(self.chain) + 1,
        'timestamp': str(datetime.datetime.now()),
        'proof': proof,
        'previous_hash': previous_hash
    }
    self.chain.append(block)
    return block
```

- **Data Structure**: Each block is a **dictionary** containing:
  - `index`: Block position in chain (integer)
  - `timestamp`: Current time (string)
  - `proof`: Proof of work value (integer)
  - `previous_hash`: Hash of previous block (string)
- **Algorithm**: Amortized O(1) list append for a fixed-size block

---

### **get_previous_block() Method**
```python
def get_previous_block(self):
    return self.chain[-1]
```

- **Algorithm**: Simple array indexing - O(1) time complexity
- Returns the last block in the chain using negative indexing

---

### **proof_of_work() Method**
```python
def proof_of_work(self, previous_proof):
    new_proof = 1
    check_proof = False
    while check_proof is False:
        hash_operation = hashlib.sha256(str(previous_proof**2 - new_proof**2).encode()).hexdigest()
        if hash_operation[:4] == '0000':
            check_proof = True
        else:
            new_proof += 1
    return new_proof
```

- **Algorithm**: **Proof of Work (PoW)** - Attempts to find a valid proof
- **Cryptographic Operation**: SHA-256 hashing
- **Logic**: 
  - Iterates incrementing `new_proof` until hash starts with '0000' (difficulty level)
  - Uses exponentiation: `previous_proof²  - new_proof²`
  - Each trial computes one digest. With four leading hexadecimal zeros and a uniform-hash model, each trial succeeds with probability $16^{-4}$, so the expected number of trials is $16^4$.

---

### **hash() Method**
```python
def hash(self, block):
    encoded_block = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(encoded_block).hexdigest()
```

- **Algorithm**: 
  - Converts block dictionary to JSON string (sorted keys for consistency)
  - Applies SHA-256 cryptographic hash function
  - Returns hexadecimal representation of the hash
- **Data Structure**: Dictionary → JSON string → bytes → hash digest

---

### **is_chain_valid() Method**
```python
def is_chain_valid(self, chain):
    if not chain:
        return False

    previous_block = None
    for index, block in enumerate(chain, start=1):
        if not isinstance(block, dict):
            return False
        block_index = block.get('index')
        if type(block_index) is not int or block_index != index:
            return False
        proof = block.get('proof')
        if type(proof) is not int or proof < 1:
            return False

        if previous_block is None:
            if proof != 1 or block.get('previous_hash') != '0':
                return False
        else:
            if block.get('previous_hash') != self.hash(previous_block):
                return False
            proof_input = str(previous_block['proof']**2 - proof**2).encode()
            if not hashlib.sha256(proof_input).hexdigest().startswith('0000'):
                return False
        previous_block = block

    return True
```

- **Algorithm**: **Linear traversal with validation** - O(n) where n = chain length
- **Verification Logic**:
  1. Checks the genesis block, consecutive indices, and positive integer proofs
  2. Checks if each later block's `previous_hash` matches the actual hash of the previous block
  3. Validates the proof of work (hash must start with '0000')
- **Data Structure**: Linear list traversal

---

## **Flask Web Application**

### **Initialization**
```python
app = Flask(__name__)
blockchain = Blockchain()
chain_lock = Lock()
```

- Creates the Flask app, the blockchain, and the lock shared by its routes

### **Routes**

#### **Index Route**
```python
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
```

- Serves HTML template (frontend interface)

#### **Mine Block Route**
```python
@app.route('/mine_block', methods=['POST'])
def mine_block():
    with chain_lock:
        previous_block = blockchain.get_previous_block()
        new_proof = blockchain.proof_of_work(previous_block['proof'])
        previous_hash = blockchain.hash(previous_block)
        block = blockchain.create_block(new_proof, previous_hash)
    response = {"block": block}
    return jsonify(response), 200
```

- **Algorithm**: Mining workflow
  - Retrieves last block
  - Performs proof of work calculation
  - Hashes previous block
  - Creates and stores the new block. The lock keeps another request from mining against the same previous block.
- **Data Structure**: Returns the mined block as JSON. The route uses POST because it changes server state.

#### **Get Chain Route**
```python
@app.route('/get_chain', methods=['GET'])
def get_chain():
    with chain_lock:
        chain = blockchain.chain.copy()
    return jsonify({'chain': chain, 'length': len(chain)}), 200
```

- Returns entire blockchain as JSON

#### **Validation Route**
```python
@app.route('/is_valid', methods=['GET'])
def is_valid():
    with chain_lock:
        chain = blockchain.chain.copy()
    is_valid = blockchain.is_chain_valid(chain)
    if is_valid:
        response = {'message': 'All good. The blockchain is valid.'}
    else:
        response = {'message': 'Error: Blockchain Not Valid'}
    return jsonify(response), 200
```

- Validates entire blockchain using the `is_chain_valid()` method

---

This is an in-memory teaching example. Its proof condition depends on consecutive proof integers rather than committing to block contents. The validation routine checks the expected genesis values, indices, adjacent links, and the toy proof condition. For example, editing the timestamp of the last block leaves those checks unchanged. Authenticating food-safety records would also require trusted data collection, authenticated inputs, and durable storage.

## **Summary of Data Structures**
| Data Structure | Use |
|---|---|
| **List** | Stores blocks in chain |
| **Dictionary** | Represents individual blocks and API responses |
| **String** | Timestamps, hashes, messages |
| **Integer** | Index, proof values |

## **Summary of Algorithms**
| Algorithm | Complexity | Purpose |
|---|---|---|
| **Proof of Work** | $16^4$ expected hash trials under the uniform-hash model | Find a proof satisfying the four-zero condition |
| **SHA-256 Hashing** | O(b) for b input bytes | Compute a digest |
| **Chain Validation** | O(n) for n fixed-size blocks | Check genesis, indices, links, and proofs |
| **List Indexing** | O(1) | Get previous block |
