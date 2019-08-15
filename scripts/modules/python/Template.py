# -*- coding: utf-8 -*

from modules.python.common.Errors_1_0 import *
from modules.python.common.RWini_1_0 import *


class Template:

	def __init__(self):
		self.errors = Errors()
		self.settings = {}
		pass

	def read_settings(self, arguments):
		rw_ini = RWini(self.errors)
		for i in range(1, len(arguments)):
			ini_file_path = arguments[i]
			rw_ini.read_settings(ini_file_path)
		
		rw_ini.copy_settings(rw_ini.settings, self.settings)
		rw_ini.compose_settings(self.settings)
	
		rw_ini.print_settings(self.settings)

	def main(self, arguments):
		self.read_settings(arguments)
		
		
		
		
		
		
		
		
		
		
		if self.errors.error_occured:
			self.errors.print_errors()
			return False

		return True
