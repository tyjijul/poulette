#!/usr/bin/python
# -*- coding: utf-8 -*-

import json, time

import os
cwd = os.path.dirname(os.path.abspath(__file__))


class libJson():

	def create_file(self):
		data = {'name': "Poulette"}
		with open('test.json', 'w') as f:
			json.dump(data, f)

	def read_file(self):
		with open('test.json') as f:
			data = json.load(f)
		return data

	def read_key(self,key):
		d = self.read_file()
		return d[key]

	def change_key(self, name, value):
		d = self.read_file()
		d[name] = value
		self.update_file(d)

	def update_file(self,data):
		with open('test.json', 'w') as f:
			json.dump(data, f)
		
	def add_key(self,key,value):
		# Ajouter une key
		d = self.read_file()
		n_key = {'new_key': 'new_value'}
		d.update(n_key)
		self.update_file(d)

if __name__ == '__main__':
	l = libJson()
	l.create_file()
	print(l.read_file())
	print(l.read_key('name'))
	# l.change_key('name',"bim")
	# print(l.read_file())
	# l.add_key("key","value")
	# print(l.read_file())