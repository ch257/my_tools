# -*- coding: utf-8 -*

class DataSetIterator:

	def __init__(self, errors, data_set, columns, index):
		pass
		# -- local columns = columns
		# -- if columns == nil or #columns == 0 then
			# -- columns = data_set['columns']
		# -- end
		# -- newObj = {
			# -- errors = errors,
			# -- eods = false,
			# -- sods = true,
			# -- row_count = 0,
			# -- data_set = data_set,
			# -- columns = columns,
			# -- rec = {},
			# -- index = index
		# -- }
		# -- self.__index = self
		# -- return setmetatable(newObj, self)
	# -- end

	# -- function DataSetIterator:get_rec()
		# -- for col_cnt=1, #self.columns do
			# -- local col_idx = self.data_set['col_idx'][self.columns[col_cnt]]
			# -- self.rec[self.columns[col_cnt]] = self.data_set.get[col_idx](self.row_count)
		# -- end
	# -- end

	# -- function DataSetIterator:get_rec_by_index()
		# -- for col_cnt=1, #self.columns do
			# -- self.rec[self.columns[col_cnt]] = self.data_set.get[col_idx](self.index[self.row_count])
		# -- end
		# -- return self.rec
	# -- end

	# -- function DataSetIterator:next_row()
		# -- self.row_count = self.row_count + 1
		# -- self.sods = false
			
		# -- if self.row_count >= #self.data_set[1] then
			# -- self.row_count = #self.data_set[1]
			# -- self.eods = true
		# -- end
		# -- self:get_rec()
		# -- return self.rec
	# -- end

	# -- function DataSetIterator:next_row_by_index()
		# -- self.row_count = self.row_count + 1
		# -- self.sods = false
			
		# -- if self.row_count >= #self.data_set[1] then
			# -- self.row_count = #self.data_set[1]
			# -- self.eods = true
		# -- end
		# -- self:get_rec_by_index()
		# -- return self.rec
	# -- end

	# -- function DataSetIterator:prev_row()
		# -- self.row_count = self.row_count - 1
		# -- self.eods = false
			
		# -- if self.row_count <= 1 then
			# -- self.row_count = 1
			# -- self.sods = true
		# -- end
		# -- self:get_rec()
		# -- return self.rec
	# -- end
