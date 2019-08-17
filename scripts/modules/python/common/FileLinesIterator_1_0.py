# -*- coding: utf-8 -*

from common.RWFile_1_0 import *

class FileLinesIterator:

	def __init__(self, errors):
		self.errors = errors
		self.file = RWFile(errors)
		self.eof = False
		self.line = None

	def read_line(self):
		self.line = self.file.read_line()
		if self.line == None:
			self.eof = True

	def open_file(self, file_path):
		self.file.open_file(file_path, 'r')
		if self.errors.error_occured:
			self.eof = True
		else:
			self.read_line()

	def close_file(self):
		self.file.close_file()

	def next_line(self):
		line = self.line
		self.read_line()
		return line
