# -*- coding: utf-8 -*

from modules.python.common.Errors_1_0 import *
from modules.python.common.RWini_1_0 import *
from modules.python.common.CSVFile_2_0 import *
from modules.python.common.DataSetIterator_2_0 import *


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
	
		# rw_ini.print_settings(self.settings)

	def main(self, arguments):
		self.read_settings(arguments)
		
		input_file_path = self.settings['files']['input_file_folder'] + self.settings['files']['input_file_name']
		input_file_format = self.settings['files']['input_file_format']
		output_file_path = self.settings['files']['output_file_folder'] + self.settings['files']['output_file_name']
		output_file_format = self.settings['files']['output_file_format']
		
		csv_file = CSVFile(self.errors)
		data_set = csv_file.read_data_set(input_file_path, input_file_format)
		
		# print(data_set)
		
		ds_iterator = DataSetIterator(self.errors, data_set)
		ds_rec = {}
		while not ds_iterator.eods:
			ds_rec = ds_iterator.next_row()
			print(ds_rec)
			break
		
		
		
		
		if self.errors.error_occured:
			self.errors.print_errors()
			return False

		return True
