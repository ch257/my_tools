# -*- coding: utf-8 -*

class RWFile:
	def __init__(self, errors):
		self.errors = errors
		self.file_handler = None

	def open_file(self, file_path, mode, encoding='utf-8'):
		try:
			self.file_handler = open(file_path, mode, encoding = encoding)
		except Exception as e:
			self.errors.raise_error('Can\'t open file "' + file_path + '"') 

	def read_line(self):
		line = self.file_handler.readline()
		if line == '':
			return None
		else:	
			return line.rstrip('\n')
	
	def write_line(self, line):
		self.file_handler.write(line + "\n")

	def close_file(self):
		if self.file_handler:
			self.file_handler.close()
			self.file_handler = None