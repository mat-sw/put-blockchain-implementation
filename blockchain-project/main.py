from blockchain import Blockchain
from client import Client
from transaction import Transaction
import os
from getpass import getpass
from typing import TypedDict
# import time
# import keyboard

class Dict(TypedDict):
    name: str
    client: Client

clients = dict()

def handleAddClient():
    os.system('cls')
    name = input('Name: ')
    passwd = getpass('Password: ')
    clients[name] = Client(passwd)
    input(f'Client named {name} has been added. Press enter to continue...')

def handleInsertMoney():
    os.system('cls')
    name = input('Name of client: ')
    if name not in clients:
        input('No client with such name. Press to continue...')
        return
    passwd = getpass()
    while not clients[name].checkPassword(passwd):
        passwd = getpass('Incorrect password. Try again or type [Q] to break... ')
        if passwd.upper() == 'Q':
            return
    os.system('cls')
    try:
        amount = int(input('Password correct. How much money do you want to insert? '))
        clients[name].payIn(amount)
    except:
        print('Wrong value. It should be numeric. Press enter to try again...')
        handleInsertMoney()

def handleShowWallet():
    os.system('cls')
    name = input('Name of client: ')
    if name not in clients:
        input('No client with such name. Press to continue...')
        return
    passwd = getpass()
    while not clients[name].checkPassword(passwd):
        passwd = getpass('Incorrect password. Try again or type [Q] to break... ')
        if passwd.upper() == 'Q':
            return
    input(f'Client has {clients[name].wallet} $ on his account. Press to continue...')

def handleCreateTransaction():
    pass

def handleViewBlockchain(blockchain : Blockchain):
    print(blockchain)

def handleViewLastBlock(blockchain : Blockchain):
    print(blockchain.getLastBlock)

if __name__ == '__main__':
    blockchain = Blockchain()
    while(True):
        os.system('cls')
        answer = input(
'''
What is your action?
[C] - Add new client
[I] - Insert money
[W] - Show clients wallet
[T] - Create transaction
[V] - View a blockchain
[L] - View last block in a chain
[Q] - Exit
... ''').upper()

        match answer:
            case 'C':
                handleAddClient()
            case 'I':
                handleInsertMoney()
            case 'W':
                handleShowWallet()
            case 'T':
                handleCreateTransaction()
            case 'V':
                handleViewBlockchain()
            case 'L':
                handleViewLastBlock()
            case 'Q':
                break
            case _:
                print("There is no known command. Let's try again...")
                input('Press enter to continue...')
                