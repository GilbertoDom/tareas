#! /usr/bin/env python3
# -*- coding:utf-8 -*-S

"""

Public Blockchain in Python 3
Gilberto Dominguez

"""

import hashlib
import datetime
from Crypto import Random
# from Crypto.Random import random
from Crypto.PublicKey import RSA
import base64


def encrypt_message(a_message, publickey):
    encrypted_msg = publickey.encrypt(a_message, 32)[0]
    encoded_encrypted_msg = base64.b64encode(encrypted_msg)  # base64 encoded strings are database friendly
    return encoded_encrypted_msg


def decrypt_message(encoded_encrypted_msg, privatekey):
    decoded_encrypted_msg = base64.b64decode(encoded_encrypted_msg)
    decoded_decrypted_msg = privatekey.decrypt(decoded_encrypted_msg)
    return decoded_decrypted_msg


class Account:
    def __init__(self, account_n, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.account_n = account_n
        self.private, self.public = self.generate_keys()

    def name(self):
        return '{} {}'.format(self.firstname, self.lastname)

    def acct(self):
        return '{}'.format(self.account_n)

    def __str__(self):
        return '{}: {}'.format(self.acct(), self.name())

    @staticmethod
    def generate_keys():
        # RSA modulus length must be a multiple of 256 and >= 1024
        modulus_length = 256*4 # use larger value in production
        # privatekey = RSA.generate(modulus_length, Random.new().read)
        privatekey = RSA.generate(modulus_length, Random.new().read)
        publickey = privatekey.publickey()
        return privatekey, publickey

    @staticmethod
    def write_msg(msg, publickey):
        return encrypt_message(msg.encode(), publickey)

    def read_msg(self, encrypted):
        return decrypt_message(encrypted, self.private)

    def get_public(self):
        return self.public

    def print_public(self):
        return self.public.exportKey()


"""
class KeyGen:
    def __init__(self):
        self.public, self.private = self.generate_keys()

    def generate_keys(self):
        # RSA modulus length must be a multiple of 256 and >= 1024
        modulus_length = 256*4 # use larger value in production
        # privatekey = RSA.generate(modulus_length, Random.new().read)
        privatekey = RSA.generate(modulus_length, Random.new().read)
        publickey = privatekey.publickey()
        return privatekey, publickey

    def get_keys(self):
        return self.public, self.private
"""


class Token:
    def __init__(self):
        pass


class Wallet:
    """ wallets have tokens """
    def __init__(self):
        pass


class Block:

    def __init__(self, index, prev_hash, data, timestamp):
        self.index = index
        self.prev_hash = prev_hash
        self.data = data
        self.creation_time = timestamp
        self.fingerprint = self.hash_header()

    def __str__(self):
        return 'Block no. {}\nCreated: {}\nContains: {}'.format(self.index, self.creation_time, self.data)

    def hash_header(self):
        m = hashlib.sha256()
        msg = '{}{}{}'.format(self.prev_hash,self.data, self.creation_time)
        m.update(msg.encode())

        return '{}'.format(m.hexdigest())


if __name__ == '__main__':

    fist_name = "Gilberto"
    last_name = "Domínguez"
    acc_no = 1

    msg = "HOLA MUNDO"

    acc = Account(acc_no, fist_name, last_name)
    acc_public = acc.get_public()
    print()
    print(acc)
    # print(acc_public)
    print(acc.write_msg(msg, acc_public).decode())
#    print()
    print(acc.read_msg(acc.write_msg(msg, acc_public)).decode())
    print()

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d - %H:%M:%S")

    m = hashlib.sha3_256()
    msg = "dksjdkdhqwoe96823i827y3g23ldseq34e"
    m.update(msg.encode())
    genesis_hash = m.hexdigest()
    # print(timestamp)
    block = Block(0, genesis_hash, "0 to 1", timestamp)
    print(block)
    print(block.fingerprint)


"""
    first, last, acc_n = 'Gilberto', 'Dominguez', 1
    acc = Account(first, last, acc_n)
    msg = 'Hola Mundo\nUwU\tMensaje Secreto'
    print(acc)
    print(acc.get_public().decode())
    enc = acc.write_msg(msg, acc.public)
    print('Encoded: {}'.format(enc.decode()))
    dec = acc.read_msg(enc)
    print('Decoded: {}'.format(dec.decode()))

    first, last, acc_n = 'Carlos', 'Aguilar', 2
    acc2 = Account(first, last, acc_n)
    msg2 = '\tMensaje Secreto'
    print(acc2)
    print(acc2.get_public().decode())
    enc = acc2.write_msg(msg2, acc2.public)
    #print(base64.)
    print('Encoded: {}'.format(enc.decode()))
    dec = acc2.read_msg(enc)
    print('Decoded: {}'.format(dec.decode()))

#for i in range(6):
#	pu, pr = acc.generate_keys()
#	print(pr.exportKey())

"""

# EOF

