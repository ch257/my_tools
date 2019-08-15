RWini = {}

function RWini:new(errors)
	newObj = {
		errors = errors,
		settings = {}
	}
	newObj.settings['ini_file_path'] = ''
	
	self.__index = self
	return setmetatable(newObj, self)
end

function RWini:parse_line(line)
	local section, param, value
	if line:match('(%;+)') == nil then
		line = string.gsub(line, '%s+', '')
		section = line:match('%[(%S+)%]')
		for p, v in string.gmatch(line, '(%S+)%=(%S+)') do 
			param = p 
			value = v
		end
	end
	return section, param, value
end

function RWini:read_settings(ini_file_path)
	local ini_file_iterator = FileLinesIterator:new(self.errors)
	ini_file_iterator:open_file(ini_file_path)
	local section, param, value, mem_section

	while not ini_file_iterator.eof do
		line = ini_file_iterator:next_line()
		section, param, value = self:parse_line(line)
		if section ~= nil then
			if self.settings[section] == nil then
				self.settings[section] = {}
				mem_section = section
			else
				mem_section = section
			end
		end
		if self.settings[mem_section] ~= nil and param ~= nil and value ~= nil then
			self.settings[mem_section][param] = value
		end
	end
	ini_file_iterator:close_file()
	self.settings['ini_file_path'] = self.settings['ini_file_path'] .. ini_file_path .. ';'
	return self.settings
end

function RWini:get_param(section, param)
	if self.settings[section] ~= nil then
		if param ~= nil then
			if self.settings[section][param] ~= nil then
				return self.settings[section][param]
			else
				self.errors:raise_error('No parameter [' .. section .. '][' .. param .. '] in ini file ' .. self.settings['ini_file_path'])
				return ''
			end
		else
			return self.settings[section]
		end
	else
		self.errors:raise_error('No section [' .. section .. '] in ini file ' .. self.settings['ini_file_path'])
		return {}
	end
end

function RWini:get_deep_param(sections, param)

end

function RWini:print_settings(settings)
	local offset = 4
	f = function(settings, offset)
		local str = ''
		for k,v in pairs(settings) do
			if type(v) == 'table' then
				str = str .. string.rep(' ', offset) .. '"' .. k .. '": {\n'
				local s = f(v, offset + offset)
				if s ~= '' then
					str = str .. string.sub(s, 1, -3) .. '\n'
				end
				str = str .. string.rep(' ', offset) .. '},\n'
			else
				str = str .. string.rep(' ', offset) .. '"' .. k .. '": "' .. v:gsub('\\', '\\\\') .. '",\n'
			end
		end
		return str
	end
	
	print('{\n' .. string.sub(f(settings, offset), 1, -3) .. '\n}')
end

function RWini:copy_settings(from_settings, to_settings, key)
	for k,v in pairs(from_settings) do
		if type(v) == 'table' then
			to_settings[k] = {}
			self:copy_settings(v, to_settings, k)
		else
			if key ~= nil then
				to_settings[key][k] = v
			else
				to_settings[k] = v
			end
		end
	end
end

function RWini:compose_settings(settings, settings_lnk)
	if settings_lnk == nil then
		settings_lnk = settings
	end
	for k,v in pairs(settings) do
		if type(v) == 'table' then
			self:compose_settings(v, settings_lnk)
		else
			if settings_lnk[v] ~= nil then
				settings[k] = settings_lnk[v]
			end
		end
	end
end
