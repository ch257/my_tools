DataSetIterator = {}

function DataSetIterator:new(errors, data_set, rec, index)
	newObj = {
		errors = errors,
		eods = false,
		sods = true,
		row_count = 0,
		data_set = data_set,
		rec = rec,
		index = index
	}
	self.__index = self
	return setmetatable(newObj, self)
end

function DataSetIterator:get_rec()
	for col_cnt=1, #self.data_set['columns'] do
		self.rec[self.data_set['columns'][col_cnt]] = self.data_set[col_cnt][self.row_count]
	end
end

function DataSetIterator:get_rec_by_index()
	for col_cnt=1, #self.data_set['columns'] do
		self.rec[self.data_set['columns'][col_cnt]] = self.data_set[col_cnt][self.index[self.row_count]]
	end
	return self.rec
end

function DataSetIterator:next_row()
	self.row_count = self.row_count + 1
	self.sods = false
		
	if self.row_count >= #self.data_set[1] then
		self.row_count = #self.data_set[1]
		self.eods = true
	end
	self:get_rec()
	return self.rec
end

function DataSetIterator:next_row_by_index()
	self.row_count = self.row_count + 1
	self.sods = false
		
	if self.row_count >= #self.data_set[1] then
		self.row_count = #self.data_set[1]
		self.eods = true
	end
	self:get_rec_by_index()
	return self.rec
end

function DataSetIterator:prev_rec()
	self.row_count = self.row_count - 1
	self.eods = false
		
	if self.row_count <= 1 then
		self.row_count = 1
		self.sods = true
	end
	self:get_rec()
	return self.rec
end
