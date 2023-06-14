from block import Block
import time
import json
from hashlib import sha256
from transaction import Transaction
from client import Client

# https://www.javatpoint.com/building-a-blockchain-using-python
# https://www.section.io/engineering-education/how-to-create-a-blockchain-in-python/
# https://www.activestate.com/blog/how-to-build-a-blockchain-in-python/
# https://gitlab.com/dsblendo/blockchain/-/blob/master/Blockchain.py
# https://www.tutorialspoint.com/python_blockchain/python_blockchain_developing_client.htm

class Blockchain: 
    difficulty = 3

    def __init__(self):
        self.unconfirmed_transactions : list[Transaction] = []
        self.chain : list[Block] = []
        self.createGenesisBlock()
    
    def __repr__(self):
        return "Blockchain()"
    
    def __str__(self):
        string = ''
        for block in self.chain:
            string += str(block)
            string += '\n'
        return string
 
    def createGenesisBlock(self):
        """
        A function to generate genesis block and appends it to
        the chain. The block has index 0, previous_hash as 0, and
        a valid hash.
        """

        genesis_block = Block(0, [], time.time(), "0")
        genesis_block.hash = genesis_block.computeHash()
        self.chain.append(genesis_block)

    @property
    def getLastBlock(self) -> Block:
        return self.chain[-1]

    def proofOfWork(self, block : Block) -> str:
        """
        A function that adds the block to the chain after verification.
        Verification includes:
        * Checking if the proof is valid.
        * The previous_hash referred in the block and the hash of latest block
          in the chain match.
        """
        block.nonce = 0
        computed_hash = block.computeHash()
        while not computed_hash.startswith('0' * Blockchain.difficulty):
            block.nonce += 1
            computed_hash = block.computeHash()
        print(f'Found matching nonce: {block.nonce}')
        print(computed_hash)
        return computed_hash

    def addBlock(self, block : Block, proof : str) -> bool:
        previous_hash = self.getLastBlock.hash
        if previous_hash != block.previous_hash:
            return False
        if not self.isProofValid(block, proof):
            return False
        block.hash = proof
        self.chain.append(block)
        return True
 
    def isProofValid(self, block : Block, block_hash : str) -> bool:
        return (block_hash.startswith('0' * Blockchain.difficulty) and
                block_hash == block.computeHash())

    def addNewTransaction(self, transaction : Transaction) -> bool:
        if transaction.proper:
            self.unconfirmed_transactions.append(transaction)
            return True
        return False
     
    def mine(self):
        if not self.unconfirmed_transactions:
            return False
 
        last_block : Block = self.getLastBlock

        new_block = Block(index=last_block.index + 1,
                          transactions=self.unconfirmed_transactions,
                          timestamp=time.time(),
                          previous_hash=last_block.hash)

        proof = self.proofOfWork(new_block)
        self.addBlock(new_block, proof)
        self.unconfirmed_transactions = []
        return new_block.index

        
# blockchain = Blockchain()

# Dinesh = Client('dinesh')
# Ramesh = Client('ramesh')
# Seema = Client('seema')
# Vijay = Client('vijay')

# Dinesh.payIn(20)

# t1 = Transaction(
#     Dinesh,
#     Ramesh,
#     15.0
# )
# t1.sign_transaction()
# t2 = Transaction(
#     Dinesh,
#     Seema,
#     6.0
# )
# t2.sign_transaction()
# t3 = Transaction(
#     Ramesh,
#     Vijay,
#     2.0
# )
# t3.sign_transaction()

# blockchain.addNewTransaction(t1)

# new_block_index = blockchain.mine()
# blockchain.addNewTransaction(t2)
# new_block_index = blockchain.mine()
# blockchain.addNewTransaction(t3)
# new_block_index = blockchain.mine()
# print(new_block_index)