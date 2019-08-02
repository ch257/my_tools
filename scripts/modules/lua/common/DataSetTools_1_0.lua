DataSetTools = {}

function DataSetTools:new(errors)
	newObj = {
		errors = errors
	}
	self.__index = self
	return setmetatable(newObj, self)
end

function DataSetTools:get_column_type(column, ds_format)
	local column_type
	if ds_format['column_type'][column] then
		column_type = ds_format['column_type'][column]
	else
		column_type = ds_format['column_type']['default']
	end
	return column_type
end

function DataSetTools:define_ds_gets_sets(data_set, col_cnt, column_type)
	if column_type == 'num' then
		data_set['get'][col_cnt] = function(row_cnt)
			if data_set[col_cnt][row_cnt] == '' then
				return nil
			else
				return data_set[col_cnt][row_cnt]
			end
		end
		data_set['set'][col_cnt] = function(row_cnt, value)
			if value == nil then
				data_set[col_cnt][row_cnt] = ''
			else
				data_set[col_cnt][row_cnt] = value
			end
		end
	else
		data_set['get'][col_cnt] = function(row_cnt)
			return data_set[col_cnt][row_cnt]
		end
		data_set['set'][col_cnt] = function(row_cnt, value)
			data_set[col_cnt][row_cnt] = value
		end
	end
end

function DataSetTools:define_rec_gets_sets(rec, column, column_type)
	if column_type == 'num' then
		rec['get'][column] = function()
			if rec[column] == '' then
				return nil
			else
				return rec[column]
			end
		end
		rec['set'][column] = function(value)
			if value == nil then
				rec[column] = ''
			else
				rec[column] = value
			end
		end
	else
		rec['get'][column] = function()
			return rec[column]
		end
		rec['set'][column] = function(value)
			rec[column] = value
		end
	end
end

function DataSetTools:create_rec(columns, ds_format)
	local rec = {}
	rec['columns'] = columns
	rec['get'] = {}
	rec['set'] = {}
	local column_type
	for col_cnt=1, #columns do
		column_type = self:get_column_type(columns[col_cnt], ds_format)
		self:define_rec_gets_sets(rec, columns[col_cnt], column_type)
		rec[columns[col_cnt]] = ''
	end
	return rec
end

function DataSetTools:create_data_set(columns, ds_format)
	local data_set = {}
	data_set['columns'] = columns
	data_set['col_idx'] = {}
	data_set['get'] = {}
	data_set['set'] = {}
	
	local column_type
	for col_cnt=1, #columns do
		data_set[col_cnt] = {}
		data_set['col_idx'][columns[col_cnt]] = col_cnt
		column_type = self:get_column_type(columns[col_cnt], ds_format)
		self:define_ds_gets_sets(data_set, col_cnt, column_type)
	end
	
	return data_set
end

function DataSetTools:add_cols(cols, col_types, data_set)
	local old_col_count = #data_set['columns']
	local new_col_count
	for col_count=1, #cols do
		new_col_count = old_col_count + col_count
		table.insert(data_set['columns'], cols[col_count])
		data_set['col_idx'][cols[col_count]] = new_col_count
		data_set[new_col_count] = {}
		self:define_ds_gets_sets(data_set, new_col_count, col_types[col_count])
		
		for row_count=1, #data_set[1] do
			table.insert(data_set[new_col_count], '')
		end
	end
end

function DataSetTools:update_row(data_set, rec, row_count)
	local k, v
	for col_count=1, #rec['columns'] do
		k = rec['columns'][col_count]
		v = rec[k]
		data_set[data_set['col_idx'][k]][row_count] = v
	end
end

function DataSetTools:insert_row(data_set, rec)
	local k, v
	local row_count = #data_set[1] + 1
	for col_count=1, #rec['columns'] do
		k = rec['columns'][col_count]
		v = rec[k]
		data_set[data_set['col_idx'][k]][row_count] = v
	end
end

