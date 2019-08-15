# -*- coding: utf-8 -*

from modules.python.common.Errors import *

class RWFile:
	def __init__(self, errors):
		errors = errors
		file_handler = None

	def open_file(self, file_path, mode):
		try:
			self.handler = open(path, mode, encoding = encoding)
		except Exception as e:
			self._errors.raise_error('Can\'t open file "' + file_path + '"') 

	def read_line(self):
		line = self.handler.readline()
		return line
	
	def write_line(self, line):
		self.handler.write(line + "\n")

	def close_file(self):
		if self.file_handler:
			self.handler.close()
			self.handler = None