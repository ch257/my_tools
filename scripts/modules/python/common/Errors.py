# -*- coding: utf-8 -*

class Errors:
	def __init__(self):
		self.errors = []
		self.error_occured = False
		
	def raise_error(self, description):
		self.error_occured = True
		self.errors.append(description)

	def print_errors(self):
		error_message = ''
		for error in self.errors:
			error_message = error_message + error + '\n'
		print(error_message)
