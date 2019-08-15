# -*- coding: utf-8 -*
import re
import sys

from modules.python.common.Errors import *
from modules.python.common.RWini import *

class Template:

	def __init__(self):
		self.errors = Errors()
		self.settings = {}
		pass

	def read_settings(self, arguments):
		rw_ini = RWini(self.errors)
		script_file_folder = (re.match(".*\\\\", sys.argv[0])).group(0)
		for i in range(1, len(arguments)):
			ini_file_path = script_file_folder + "..\\" + arguments[i]
			print(arguments[i])
			rw_ini.read_settings(ini_file_path)
		
	# rw_ini:copy_settings(rw_ini.settings, self.settings, nil)
	# rw_ini:compose_settings(self.settings)
	
	# -- rw_ini:print_settings(self.settings)
# end
		pass

	def main(self, arguments):
		self.read_settings(arguments)
		return True
