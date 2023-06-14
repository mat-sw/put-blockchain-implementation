
import binascii
import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

class Client:
   _wallet: float
   __password : str

   def __init__(self, passwd):
      random = Crypto.Random.new().read
      self._private_key = RSA.generate(1024, random)
      self._public_key = self._private_key.publickey()
      self._signer = PKCS1_v1_5.new(self._private_key)
      self._wallet = 0
      self.__password = passwd

   @property
   def identity(self) -> str:
      return binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')

   @property
   def wallet(self) -> float:
      return self._wallet
   
   def withdraw(self, amount : float) -> bool:
      if amount > self._wallet:
         return False
      self._wallet -= amount
      return True
   
   def payIn(self, amount : float) -> None:
      self._wallet += amount
   
   def checkPassword(self, passwd) -> bool:
      if (passwd == self.__password):
         return True
      return False