# -*- coding: utf-8 -*

from modules.python.common.Errors import *
from modules.python.common.FileLinesIterator import *

class RWini:

	def __init__(self, errors):
		self.errors = errors
		self.settings = {}
		self.settings['ini_file_path'] = ''

	def parse_line(self, line):
		section, param, value = None, None, None
		line = line.rstrip(' \t').lstrip(' \t')
		commebt_smb_pos = line.find(';')
		if commebt_smb_pos > -1:
			line = line[0:commebt_smb_pos]
		
		if line != '':
			if line[0:1] == '[' and line[-1:] == ']':
				section = line[1:-1]
			else:
				eq_smb_pos = line.find('=')
				param = line[0:eq_smb_pos].rstrip(' \t')
				value = line[eq_smb_pos + 1:].lstrip(' \t')
		return section, param, value

	def read_settings(self, ini_file_path):
		ini_file_iterator = FileLinesIterator(self.errors)
		ini_file_iterator.open_file(ini_file_path)
		section, param, value, mem_section = None, None, None, None

		cnt = 1
		while not ini_file_iterator.eof:
			line = ini_file_iterator.next_line()
			section, param, value = self.parse_line(line)
			if section != None:
				if self.settings.get(section) == None:
					self.settings[section] = {}
					mem_section = section
				else:
					mem_section = section
			if self.settings.get(mem_section) != None and param != None and value != None:
				self.settings[mem_section][param] = value
			
		ini_file_iterator.close_file()
		self.settings['ini_file_path'] = self.settings['ini_file_path'] + ini_file_path + ';'
		return self.settings

# function RWini:get_param(section, param)
	# if self.settings[section] ~= nil then
		# if param ~= nil then
			# if self.settings[section][param] ~= nil then
				# return self.settings[section][param]
			# else
				# self.errors:raise_error('No parameter [' .. section .. '][' .. param .. '] in ini file ' .. self.settings['ini_file_path'])
				# return ''
			# end
		# else
			# return self.settings[section]
		# end
	# else
		# self.errors:raise_error('No section [' .. section .. '] in ini file ' .. self.settings['ini_file_path'])
		# return {}
	# end
# end

# function RWini:get_deep_param(sections, param)

# end

	def print_settings(self, settings):
		offset = 4
		print(settings)
		def f (settings, offset):
			str = ''
			for k in settings:
				v = settings[k]
				if type(v) == dict:
					str = str + ' '*offset + '"' + k + '": {\n'
					s = f(v, offset + offset)
					if s != '':
						str = str + s[0: -2] + '\n'
					str = str + ' '*offset + '},\n'
				else:
					str = str + ' '*offset + '"' + k + '": "' + v.replace('\\', '\\\\') + '",\n'
			return str
		
		print('{\n' + f(settings, offset)[1: -2] + '\n}')

# function RWini:copy_settings(from_settings, to_settings, key)
	# for k,v in pairs(from_settings) do
		# if type(v) == 'table' then
			# to_settings[k] = {}
			# self:copy_settings(v, to_settings, k)
		# else
			# if key ~= nil then
				# to_settings[key][k] = v
			# else
				# to_settings[k] = v
			# end
		# end
	# end
# end

# function RWini:compose_settings(settings, settings_lnk)
	# if settings_lnk == nil then
		# settings_lnk = settings
	# end
	# for k,v in pairs(settings) do
		# if type(v) == 'table' then
			# self:compose_settings(v, settings_lnk)
		# else
			# if settings_lnk[v] ~= nil then
				# settings[k] = settings_lnk[v]
			# end
		# end
	# end
# end
