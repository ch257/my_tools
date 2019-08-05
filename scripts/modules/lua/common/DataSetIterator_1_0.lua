DataSetIterator = {}

function DataSetIterator:new(errors, data_set, index)
	newObj = {
		errors = errors,
		eods = false,
		sods = true,
		row_count = 0,
		data_set = data_set,
		index = index
	}
	self.__index = self
	return setmetatable(newObj, self)
end

function DataSetIterator:get_rec(rec)
	for col_cnt=1, #self.data_set['columns'] do
		rec[self.data_set['columns'][col_cnt]] = self.data_set[col_cnt][self.row_count]
	end
end

function DataSetIterator:get_rec_by_index(rec)
	for col_cnt=1, #self.data_set['columns'] do
		rec[self.data_set['columns'][col_cnt]] = self.data_set[col_cnt][self.index[self.row_count]]
	end
end

function DataSetIterator:next_row(rec)
	self.row_count = self.row_count + 1
	self.sods = false
		
	if self.row_count >= #self.data_set[1] then
		self.row_count = #self.data_set[1]
		self.eods = true
	end
	self:get_rec(rec)
end

function DataSetIterator:next_row_by_index(rec)
	self.row_count = self.row_count + 1
	self.sods = false
		
	if self.row_count >= #self.data_set[1] then
		self.row_count = #self.data_set[1]
		self.eods = true
	end
	self:get_rec_by_index(rec)
end

function DataSetIterator:prev_rec(rec)
	self.row_count = self.row_count - 1
	self.eods = false
		
	if self.row_count <= 1 then
		self.row_count = 1
		self.sods = true
	end
	self:get_rec(rec)
end
