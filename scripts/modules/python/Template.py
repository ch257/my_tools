class Template:

	def __init__(self):
		pass

	def read_settings(self, arguments):
	# local rw_ini = RWini:new(self.errors)
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
		self:read_settings(arguments)
		return True