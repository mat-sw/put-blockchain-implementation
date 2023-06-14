from hashlib import sha256
import json
from transaction import Transaction
from datetime import datetime

class Block:
    hash : str

    def __init__(self, index, transactions, timestamp, previous_hash, nonce=0):
        self.index : int = index
        self.transactions : list[Transaction] = transactions
        self.timestamp : float = timestamp
        self.previous_hash : str = previous_hash
        self.nonce = nonce
    
    def __repr__(self) -> str:
        return 'Block()'
    
    def __str__(self) -> str:
        return f'[Index : {self.index}, Timestamp : {datetime.fromtimestamp(self.timestamp)}, Nonce : {self.nonce}, Hash: {self.hash}, Transactions : {len(self.transactions)}]'
    
    def computeHash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()

    def dict(self):
        return self.__dict__

    