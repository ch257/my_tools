# -*- coding: utf-8 -*

from modules.python.common.Errors import *

class Template:

	def __init__(self):
		self.errors = Errors()
		self.settings = []
		pass

	def read_settings(self, arguments):
		rw_ini = RWini(self.errors)
	# for i = 1, #arguments do
		# local ini_file_path = script_file_folder .. "..\\" .. arguments[i]
		# rw_ini:read_settings(ini_file_path)
	# end

	# rw_ini:copy_settings(rw_ini.settings, self.settings, nil)
	# rw_ini:compose_settings(self.settings)
	
	# -- rw_ini:print_settings(self.settings)
# end
		pass

	def main(self, arguments):
		self.read_settings(arguments)
		return True
