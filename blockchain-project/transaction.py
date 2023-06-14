import time
from client import Client
import binascii
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5

class Transaction(dict):
   _proper : bool

   def __init__(self, sender : Client, recipient : Client, value : float):
      self.sender : Client = sender
      self.recipient : Client = recipient
      self.value : float = value
      self.time = int(time.time())
      self.checkTransaction()

   def __str__(self) -> str:
      return self.__dict__
   
   def __repr__(self) -> str:
      return self.__dict__
   
   def checkTransaction(self):
      if self.sender.wallet < self.value:
         self._proper = False
         return
      self._proper = True
      self.sender.withdraw(self.value)
      self.recipient.payIn(self.value)
   
   @property
   def proper(self) -> bool:
      return self._proper
   
   def to_dict(self):
      if self.sender == "Genesis":
         identity = "Genesis"
      else:
         identity = self.sender.identity

      return {
         'sender': identity,
         'recipient': self.recipient.identity,
         'value': self.value,
         'time' : self.time
      }

   def sign_transaction(self) -> str:
      private_key = self.sender._private_key
      signer = PKCS1_v1_5.new(private_key)
      h = SHA.new(str(self.to_dict()).encode('utf8'))
      return binascii.hexlify(signer.sign(h)).decode('ascii')
    

def display_transaction(transaction : Transaction):
   #for transaction in transactions:
   dict = transaction.to_dict()
   print ("sender: " + dict['sender'])
   print ('-----')
   print ("recipient: " + dict['recipient'])
   print ('-----')
   print ("value: " + str(dict['value']))
   print ('-----')
   print ("time: " + str(dict['time']))
   print ('-----')

transactions = []

# Dinesh = Client('dinesh')
# Ramesh = Client('ramesh')
# Seema = Client('seema')
# Vijay = Client('vijay')
# t1 = Transaction(
#    Dinesh,
#    Ramesh.identity,
#    15.0
# )
# t1.sign_transaction()
# transactions.append(t1)
# t2 = Transaction(
#    Dinesh,
#    Seema.identity,
#    6.0
# )
# t2.sign_transaction()
# transactions.append(t2)
# t3 = Transaction(
#    Ramesh,
#    Vijay.identity,
#    2.0
# )
# t3.sign_transaction()
# transactions.append(t3)
# t4 = Transaction(
#    Seema,
#    Ramesh.identity,
#    4.0
# )
# t4.sign_transaction()
# transactions.append(t4)
# t5 = Transaction(
#    Vijay,
#    Seema.identity,
#    7.0
# )
# t5.sign_transaction()
# transactions.append(t5)
# t6 = Transaction(
#    Ramesh,
#    Seema.identity,
#    3.0
# )
# t6.sign_transaction()
# transactions.append(t6)
# t7 = Transaction(
#    Seema,
#    Dinesh.identity,
#    8.0
# )
# t7.sign_transaction()
# transactions.append(t7)
# t8 = Transaction(
#    Seema,
#    Ramesh.identity,
#    1.0
# )
# t8.sign_transaction()
# transactions.append(t8)
# t9 = Transaction(
#    Vijay,
#    Dinesh.identity,
#    5.0
# )
# t9.sign_transaction()
# transactions.append(t9)
# t10 = Transaction(
#    Vijay,
#    Ramesh.identity,
#    3.0
# )
# t10.sign_transaction()
# transactions.append(t10)

# for transaction in transactions:
#    display_transaction (transaction)
#    print ('--------------')
