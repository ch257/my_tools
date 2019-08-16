# -*- coding: utf-8 -*

class DataSetIterator:

	def __init__(self, errors, data_set, columns={}, index=None):
		self.columns = columns
		if len(columns) == 0:
			self.columns = data_set['columns']
		self.errors = errors
		self.eods = False
		self.sods = True
		self.row_count = -1
		self.data_set = data_set
		self.rec = {}
		self.index = index

	def get_rec(self):
		for col_cnt in range(len(self.columns)):
			col_idx = self.data_set['col_idx'][self.columns[col_cnt]]
			self.rec[self.columns[col_cnt]] = self.data_set[col_idx][self.row_count]

	# function DataSetIterator:get_rec_by_index()
		# for col_cnt=1, #self.columns do
			# self.rec[self.columns[col_cnt]] = self.data_set.get[col_idx](self.index[self.row_count])
		# end
		# return self.rec
	# end

	def next_row(self):
		self.row_count = self.row_count + 1
		self.sods = False
		if self.row_count > len(self.data_set[0]) - 1:
			self.row_count = len(self.data_set[0]) - 1
			self.eods = True
		self.get_rec()
		return self.rec

	# function DataSetIterator:next_row_by_index()
		# self.row_count = self.row_count + 1
		# self.sods = false
			
		# if self.row_count >= #self.data_set[1] then
			# self.row_count = #self.data_set[1]
			# self.eods = true
		# end
		# self:get_rec_by_index()
		# return self.rec
	# end

	# function DataSetIterator:prev_row()
		# self.row_count = self.row_count - 1
		# self.eods = false
			
		# if self.row_count <= 1 then
			# self.row_count = 1
			# self.sods = true
		# end
		# self:get_rec()
		# return self.rec
	# end
