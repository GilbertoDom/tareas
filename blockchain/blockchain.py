#! /usr/bin/env python3
# -*- coding:utf-8 -*-S

"""

Public Blockchain in Python 3
Gilberto Dominguez

"""

import hashlib
import datetime
from Crypto import Random
from Crypto.Random import random
from Crypto.PublicKey import RSA
import base64



class Account:
	def __init__(self, firstname, lastname, account_n):
		self.firstname = firstname
		self.lastname = lastname
		self.account_n = account_n
		self.private, self.public = self.generate_keys()


	def Name(self):
		return '{} {}'.format(self.firstname, self.lastname)
	def Acct(self):
		return '{}'.format(self.account_n)
	def __str__(self):
		return '{}: {}'.format(self.Acct(), self.Name())

	def generate_keys(self):
		o = KeyGen()
		public, private = o.get_keys()
		return public, private

		"""
		# RSA modulus length must be a multiple of 256 and >= 1024
		modulus_length = 256*4 # use larger value in production
		#privatekey = RSA.generate(modulus_length, Random.new().read)
		privatekey = RSA.generate(modulus_length, Random.new().read)
		publickey = privatekey.publickey()
		return privatekey, publickey
		"""
	def encrypt_message(self, a_message , publickey):
		encrypted_msg = publickey.encrypt(a_message, 32)[0]
		encoded_encrypted_msg = base64.b64encode(encrypted_msg) # base64 encoded strings are database friendly
		return encoded_encrypted_msg

	def decrypt_message(self, encoded_encrypted_msg, privatekey):
		decoded_encrypted_msg = base64.b64decode(encoded_encrypted_msg)
		decoded_decrypted_msg = privatekey.decrypt(decoded_encrypted_msg)
		return decoded_decrypted_msg

	def write_msg(self, msg, publickey):
		return self.encrypt_message(msg.encode('utf-8'), publickey)

	def read_msg(self, encrypted):
		return self.decrypt_message(encrypted, self.private)

	def get_public(self):
		#return '{}'.format(self.public.exportKey().decode())
		return self.public.exportKey()

class KeyGen:
	def __init__(self):
		self.public, self.private = self.generate_keys()

	def generate_keys(self):
		# RSA modulus length must be a multiple of 256 and >= 1024
		modulus_length = 256*4 # use larger value in production
		#privatekey = RSA.generate(modulus_length, Random.new().read)
		privatekey = RSA.generate(modulus_length, Random.new().read)
		publickey = privatekey.publickey()
		return privatekey, publickey

	def get_keys(self):
		return self.public, self.private

class Token:
	def __init__(self):
		pass

class Wallet:
	""" wallets have tokens """
	def __init__(self):
		pass

class Block:
	def __init__(self, index, prev_hash, data, timestamp):
		#self.hash = None
		self.index = index
		self.prev_hash = prev_hash
		self.data = data
		self.creation_time = timestamp
		self.hash_ = self.calculate_hash()

	def calculate_hash(self):
		m = hashlib.sha256()
		msg = '{}{}{}{}'.format(self.index, self.prev_hash,self.data, self.creation_time)
		m.update(msg.encode())
		#print(m.hexdigest())
		return '{}'.format(m.hexdigest())


if __name__ == '__main__':

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

	for i in range(6):
		pu, pr = acc.generate_keys()
		print(pr.exportKey())


