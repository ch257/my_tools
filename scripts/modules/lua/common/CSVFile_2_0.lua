CSVFile = {}

function CSVFile:new(errors)
	newObj = {
		errors = errors
	}
	self.__index = self
	return setmetatable(newObj, self)
end

function CSVFile:define_cast_functions(columns, file_format)
	local cast = {}
	
	set_func = function(col_cnt, value_type, cast)
		if value_type == 'num' then
			cast[col_cnt] = function(value)
				if value == '' then
					return value
				else
					return tonumber(value)
				end
			end
		elseif value_type == 'str' then
			cast[col_cnt] = function(value)
				return value
			end
		elseif value_type == 'ddmmyy' then
			cast[col_cnt] = function(value)
				return {
					day = tonumber(string.sub(value, 1,2)),
					month = tonumber(string.sub(value, 3,4)),
					year = tonumber(string.sub(value, 5,6))
				}
			end
		elseif value_type == 'yyyymmdd' then
			cast[col_cnt] = function(value)
				return {
					day = tonumber(string.sub(value, 7,8)),
					month = tonumber(string.sub(value, 5,6)),
					year = tonumber(string.sub(value, 1,4))
				}
			end
		elseif value_type == 'hhmmss' then
			cast[col_cnt] = function(value)
				return {
					hour = tonumber(string.sub(value, 1,2)),
					min = tonumber(string.sub(value, 3,4)),
					sec = tonumber(string.sub(value, 5,6))
				}
			end
		else
			cast[col_cnt] = function(value)
				self.errors:raise_error('Unknown type for column \'' .. tostring(columns[col_cnt]))
				return 'UnknownType'
			end
		end
	end
	
	for col_cnt=1, #columns do
		if file_format['column_type'][columns[col_cnt]] then
			value_type = file_format['column_type'][columns[col_cnt]]
		else
			value_type = file_format['column_type']['default']
		end
		set_func(col_cnt, value_type, cast)
	end
	
	return cast
end

function CSVFile:define_format_str_functions(columns, file_format)
	local format_str = {}
	
	set_func = function(col_cnt, str_template, value_type, format_str)
		if value_type == 'num' then
			format_str[col_cnt] = function(value)
				if value == '' then
					return value
				else
					return string.format(str_template, value)
				end
			end
		elseif value_type == 'str' then
			format_str[col_cnt] = function(value)
				return value
			end
		elseif value_type == 'ddmmyy' then
			format_str[col_cnt] = function(value)
				return string.format(str_template, 
					string.format('%02d', value['day']), 
					string.format('%02d',value['month']), 
					string.format('%02d',value['year']))
			end
		elseif value_type == 'yyyymmdd' then
			format_str[col_cnt] = function(value)
				return string.format(str_template, 
					tostring(value['year']), 
					string.format('%02d',value['month']), 
					string.format('%02d',value['day']))
			end
		elseif value_type == 'hhmmss' then
			format_str[col_cnt] = function(value)
				return string.format(str_template, 
					string.format('%02d',value['hour']), 
					string.format('%02d',value['min']), 
					string.format('%02d',value['sec']))
			end
		else
			format_str[col_cnt] = function(value)
				self.errors:raise_error('Unknown format for column \'' .. tostring(columns[col_cnt]))
				return 'UnknownFormat'
			end
		end
	
	end
	
	for col_cnt=1, #columns do
		if file_format['column_format'][columns[col_cnt]] then
			str_template = file_format['column_format'][columns[col_cnt]]
		else
			str_template = file_format['column_format']['default']
		end
		if file_format['column_type'][columns[col_cnt]] then
			value_type = file_format['column_type'][columns[col_cnt]]
		else
			value_type = file_format['column_type']['default']
		end
		set_func(col_cnt, str_template, value_type, format_str)
	end
	return format_str
end

function CSVFile:define_columns(file_path, file_format)
	local columns = {}
	local string_tools = StringTools:new(errors)
	local column_separator = file_format['column_separator']
	local file = RWFile:new(self.errors)
	
	file:open_file(file_path, 'r')
	if self.errors.error_occured then
		return columns
	end

	if file_format['has_header'] == '1' then
		line = file:read_line()
		if line ~= nil then
			columns = string_tools:split(line, column_separator)
		end
	else
		line = file:read_line()
		if line ~= nil then
			for i = 1, #string_tools:split(line, column_separator) do
				table.insert(columns, i)
			end
		end
	end
	file:close_file()
	return columns
end

function CSVFile:read_data_set(file_path, file_format)
	local data_set = {}
	local cast = {}
	local string_tools = StringTools:new(errors)
	local ds_tools = DataSetTools:new(errors)
	local file = RWFile:new(self.errors)
	
	local columns = self:define_columns(file_path, file_format)
	local cast = self:define_cast_functions(columns, file_format)
	
	data_set = ds_tools:create_data_set(columns, file_format)
	
	file:open_file(file_path, 'r')
	if file_format['has_header'] == '1' then
		line = file:read_line()
	end
	
	local column_separator = file_format['column_separator']
	while not self.errors.error_occured do
		line = file:read_line()
		if line == nil then
			break
		end
		if line ~= '' then
			row_data = string_tools:split(line, column_separator)
			for col_cnt=1, #data_set['columns'] do
				table.insert(data_set[col_cnt], cast[col_cnt](row_data[col_cnt]))
			end
		end
		-- break
	end
	file:close_file()
	
	return data_set
end

function CSVFile:write_data_set(data_set, columns, file_path, file_format)
	local string_tools = StringTools:new(errors)
	local file = RWFile:new(self.errors)
	local line = ''
	local column_separator = file_format['column_separator']
	
	local columns = columns
	if columns == nil or #columns == 0 then
		columns = data_set['columns']
	end
	
	local format_str = self:define_format_str_functions(data_set['columns'], file_format)
	
	file:open_file(file_path, 'w')
	if self.errors.error_occured then
		return nil
	end
	
	if file_format['has_header'] == '1' then
		for col_cnt=1, #columns do
			line = line .. tostring(columns[col_cnt]) .. column_separator
		end
		if line ~= '' then
			file:write_line(string.sub(line, 1, -(string.len(column_separator) + 1)))
		end
	end
	
	if data_set[1] ~= nil then
		for row_cnt=1, #data_set[1] do
			line = ''
			for col_cnt=1, #columns do
				local col_idx = data_set['col_idx'][columns[col_cnt]]
				line = line .. format_str[col_idx](data_set[col_idx][row_cnt]) .. column_separator
			end
			if line ~= '' then
				file:write_line(string.sub(line, 1, -(string.len(column_separator) + 1)))
			end
			-- break
		end
	end
	file:close_file()
end

function CSVFile:print_data_set(data_set, columns, file_format)
	local line = ''
	local column_separator = file_format['column_separator']
	local format_str = self:define_format_str_functions(data_set['columns'], file_format)
	
	local columns = columns
	if columns == nil or #columns == 0 then
		columns = data_set['columns']
	end
	
	for col_cnt=1, #columns do
		line = line .. tostring(columns[col_cnt]) .. column_separator
	end
	if line ~= '' then
		print(string.sub(line, 1, -(string.len(column_separator) + 1)))
	end
	
	if data_set[1] ~= nil then
		for row_cnt=1, #data_set[1] do
			line = ''
			for col_cnt=1, #columns do
				local col_idx = data_set['col_idx'][columns[col_cnt]]
				line = line .. format_str[col_idx](data_set[col_idx][row_cnt]) .. column_separator
			end
			if line ~= '' then
				print(string.sub(line, 1, -(string.len(column_separator) + 1)))
			end
			-- break
		end
	end
end

function CSVFile:create_csv_iterator(file_path, file_format, columns)
	local csv_file = CSVFile:new(self.errors)
	local data_set = csv_file:read_data_set(file_path, file_format)
	local ds_iterator = DataSetIterator:new(self.errors, data_set, columns)
	
	return ds_iterator
end
