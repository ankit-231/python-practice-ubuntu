import hashlib
import datetime

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        return hashlib.sha256((str(self.index) + self.timestamp + str(self.data) + self.previous_hash).encode('utf-8')).hexdigest()

def create_genesis_block():
    return Block(0, str(datetime.datetime.now()), "Genesis Block", "0")

blockchain = [create_genesis_block()]

def add_block(data):
    previous_block = blockchain[-1]
    index = previous_block.index + 1
    timestamp = str(datetime.datetime.now())
    previous_hash = previous_block.hash
    return Block(index, timestamp, data, previous_hash)

# Example usage:
blockchain.append(add_block("This is block 2"))
blockchain.append(add_block("This is block 3"))

for block in blockchain:
    print(f"Block #{block.index}: {block.data}, Hash: {block.hash}")
