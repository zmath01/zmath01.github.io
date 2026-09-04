# blockchain-food-safety

Line-by-Line Explanation of Data Structures and Algorithms

<!--more-->

## **Imports (Lines 1-4)**
```python
import datetime
import hashlib
import json
from flask import Flask, jsonify, render_template
```

- **datetime**: Standard library for timestamp generation
- **hashlib**: Cryptographic hashing library (SHA-256)
- **json**: For serializing objects to JSON format
- **Flask**: Web framework for creating REST API endpoints

---

## **Blockchain Class Definition (Line 6)**

### **Constructor (Lines 7-9)**
```python
def __init__(self):
    self.chain = []
    self.create_block(proof=1, previous_hash='0')
```

- **Data Structure**: `self.chain` is a **list** that stores all blocks in the blockchain
- **Algorithm**: Genesis block creation - initializes the chain with the first block

---

### **create_block() Method (Lines 11-20)**
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
- **Algorithm**: O(1) time complexity - appends block to list

---

### **get_previous_block() Method (Lines 22-23)**
```python
def get_previous_block(self):
    return self.chain[-1]
```

- **Algorithm**: Simple array indexing - O(1) time complexity
- Returns the last block in the chain using negative indexing

---

### **proof_of_work() Method (Lines 25-33)**
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
  - Time complexity: O(n) where n depends on mining difficulty

---

### **hash() Method (Lines 35-37)**
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

### **is_chain_valid() Method (Lines 39-51)**
```python
def is_chain_valid(self, chain):
    previous_block = chain[0]
    block_index = 1
    while block_index < len(chain):
        block = chain[block_index]
        if block['previous_hash'] != self.hash(previous_block):
            return False
        hash_operation = hashlib.sha256(str(previous_block['proof']**2 - block['proof']**2).encode()).hexdigest()
        if hash_operation[:4] != '0000':
            return False
        previous_block = block
        block_index += 1
    return True
```

- **Algorithm**: **Linear traversal with validation** - O(n) where n = chain length
- **Verification Logic**:
  1. Checks if each block's `previous_hash` matches the actual hash of the previous block
  2. Validates the proof of work (hash must start with '0000')
  3. Continues through entire chain
- **Data Structure**: Linear list traversal

---

## **Flask Web Application (Lines 53-75)**

### **Initialization (Lines 53-54)**
```python
app = Flask(__name__)
blockchain = Blockchain()
```

- Creates Flask app instance and blockchain instance

### **Routes**

#### **Index Route (Lines 55-57)**
```python
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
```

- Serves HTML template (frontend interface)

#### **Mine Block Route (Lines 58-72)**
```python
@app.route('/mine_block', methods=['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    new_proof = blockchain.proof_of_work(previous_block['proof'])
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(new_proof, previous_hash)
    response = {...}
    return jsonify(response), 200
```

- **Algorithm**: Mining workflow
  - Retrieves last block
  - Performs proof of work calculation
  - Hashes previous block
  - Creates and stores new block
- **Data Structure**: Returns JSON response (dictionary)

#### **Get Chain Route (Lines 73-78)**
```python
@app.route('/get_chain', methods=['GET'])
def get_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200
```

- Returns entire blockchain as JSON

#### **Validation Route (Lines 79-86)**
```python
@app.route('/is_valid', methods=['GET'])
def is_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response = {'message': 'All good. The blockchain is valid.'}
    else:
        response = {'message': 'Error: Blockchain Not Valid'}
    return jsonify(response), 200
```

- Validates entire blockchain using the `is_chain_valid()` method

---

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
| **Proof of Work** | O(n) | Mining difficulty/security |
| **SHA-256 Hashing** | O(1) | Block integrity verification |
| **Chain Validation** | O(n) | Detect tampering |
| **Linear Search** | O(1) avg | Get previous block |
