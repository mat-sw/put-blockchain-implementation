from blockchain import Blockchain
from client import Client
from transaction import Transaction
import os
from getpass import getpass
import time

clients = dict()

def checkingMiningPossibilities(blockchain: Blockchain):
    os.system('cls')
    print('Checking if mining can be done...')
    time.sleep(2)
    if len(blockchain.unconfirmed_transactions) >= 2:
        print('Mining...')
        blockchain.mine()
        input(f'New block with hash {blockchain.getLastBlock.hash} add. Press to continue...')
    else:
        print('No transactions to use. Redirecting to GUI...')
        time.sleep(2)

def handleAddClient():
    os.system('cls')
    print('ADDING NEW CLIENT')
    name = input('Name: ')
    passwd = getpass('Password: ')
    clients[name] = Client(passwd)
    input(f'Client named `{name}` has been added. Press enter to continue...')

def listClients():
    print('')
    for key in clients:
        print(key)
    print('')

def handleListClients():
    os.system('cls')
    print('List of all the clients:')
    listClients()
    input('Press to continue...')

def handleInsertMoney():
    os.system('cls')
    print('MONEY INSERTION')
    listClients()
    name = input('Name of client from the list: ')
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
        input('Wrong value. It should be numeric. Press enter to try again...')
        handleInsertMoney()

def handleShowWallet():
    os.system('cls')
    print('CHECK WALLET')
    listClients()
    name = input('Name of client from the list: ')
    if name not in clients:
        input('No client with such name. Press to continue...')
        return
    passwd = getpass()
    while not clients[name].checkPassword(passwd):
        passwd = getpass('Incorrect password. Try again or type [Q] to break... ')
        if passwd.upper() == 'Q' or passwd.upper() == 'EXIT':
            return
    input(f'Client has {clients[name].wallet} $ on his account. Press to continue...')

def handleCreateTransaction():
    os.system('cls')
    print('CREATE TRANSACTION')
    listClients()
    sender = input('Sender name from the list: ')
    if sender not in clients:
        input('No client with such name. Press to continue...')
        return
    recipient = input('Recipient name from the list: ')
    if recipient not in clients:
        input('No client with such name. Press to continue...')
        return
    try:
        value = int(input('Transaction value: '))
    except:
        input('Wrong value. It should be numeric. Press enter to try again...')
        handleCreateTransaction()
    passwd = getpass('Sender\'s password: ')
    while not clients[sender].checkPassword(passwd):
        passwd = getpass('Incorrect password. Try again or type [Q] to break... ')
        if passwd.upper() == 'Q' or passwd.upper() == 'EXIT':
            return
    transaction = Transaction(clients[sender], clients[recipient], value)
    transaction.sign_transaction()
    if blockchain.addNewTransaction(transaction):
        input('Transaction correct. Now it is waiting for a new block. Press to continue...')
    else:
        input('Incorrect transaction. Activity dumped. Press to continue...')


def handleViewBlockchain(blockchain : Blockchain):
    input(f'{blockchain}\n\nPress enter to continue...')

def handleViewLastBlock(blockchain : Blockchain):
    input(f'{blockchain.getLastBlock}\n\nPress enter to continue...')

if __name__ == '__main__':
    blockchain = Blockchain()
    while(True):
        # os.system('cls')
        # print('Checking if mining can be done...')
        # time.sleep(2)
        # if len(blockchain.unconfirmed_transactions) >= 2:
        #     blockchain.mine()
        # else:
        #     print('No transactions to use. Redirecting to GUI...')
        #     time.sleep(2)
        os.system('cls')
        answer = input(
'''
What is your action?
[C] - Add new client
[I] - Insert money
[W] - Show clients wallet
[L] - List all the clients
[T] - Create transaction
[V] - View a blockchain
[B] - View last block in a chain
[Q] - Exit
... ''').upper()

        match answer:
            case 'C':
                handleAddClient()
            case 'I':
                handleInsertMoney()
            case 'W':
                handleShowWallet()
            case 'L':
                handleListClients()
            case 'T':
                handleCreateTransaction()
                checkingMiningPossibilities(blockchain)
            case 'V':
                handleViewBlockchain(blockchain)
            case 'B':
                handleViewLastBlock(blockchain)
            case 'Q':
                break
            case _:
                print("There is no known command. Let's try again...")
                input('Press enter to continue...')
                