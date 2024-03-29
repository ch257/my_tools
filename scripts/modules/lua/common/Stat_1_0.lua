Stat = {}

function Stat:new(errors, stat_data_format)
	newObj = {
		errors = errors,
		stat_data_format = stat_data_format
	}
	self.__index = self
	return setmetatable(newObj, self)
end

function Stat:hist(data_set, column, window)
	local ds_tools = DataSetTools:new(self.errors)
	local column = ds_tools:copy_column(data_set, '<BC/BA>')
	ds_tools:sort_column(column)
	local hist = ds_tools:create_data_set({'<X>','<FREQ>','<PERC>'}, self.stat_data_format)
	local hist_rec = {}
	
	local start_x = column[1] - column[1] % window
	local end_x = column[#column] - column[#column] % window + window
	local next_x
	
	local col_cnt = 1
	local freq = 0
	while col_cnt <= #column and start_x <= end_x do
		next_x = start_x + window
		freq = 0
		while col_cnt <= #column and column[col_cnt] < next_x do
			col_cnt = col_cnt + 1
			freq = freq + 1
		end
		
		hist_rec['<X>'] = next_x
		hist_rec['<FREQ>'] = freq
		hist_rec['<PERC>'] = freq/#column * 100
		ds_tools:insert_row(hist, hist_rec)
		
		start_x = next_x
	end
	return hist
end


