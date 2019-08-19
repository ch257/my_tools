Logger = {}

function Logger:new(errors)
	newObj = {
		errors = errors,
		data_set,
		events = {},
		chunk_length,
		after_event_length,
		file_folder,
		file_name_prefix,
		file_ext,
		log_file_format,
		file_count
	}
	self.__index = self
	return setmetatable(newObj, self)
end

function Logger:init(settings, data_set)
	local fs = FS:new(self.errors)
	self.data_set = data_set
	self.chunk_length = tonumber(settings['chunk_length'])
	self.after_event_length = tonumber(settings['after_event_length'])
	self.file_folder = settings['file_folder']
	self.file_name_prefix = settings['file_name_prefix']
	self.file_ext = settings['file_ext']
	self.log_file_format = settings['log_file_format']
	self.file_count = 1
	fs:clear_folder(self.file_folder)
end

function Logger:add_event(index)
	table.insert(self.events, index)
end

function Logger:auto_save_events(index)
	local to_remove = {}
	local offset = 0
	local start_index
	for i = 1, #self.events do
		if index - self.events[i] >= self.after_event_length then
			start_index = index - self.chunk_length + 1
			if start_index < 1 then
				start_index = 1
			end
			self:save(start_index, index)
			-- print(tostring(start_index) .. ':' .. tostring(index))
			table.insert(to_remove, i - offset)
			offset = offset + 1
		end
	end
	for i = 1, #to_remove do
		table.remove(self.events, to_remove[i])
	end
end

function Logger:save_remained_events(index)
	local start_index
	for i = 1, #self.events do
		start_index = self.events[i] - (self.chunk_length - self.after_event_length) + 1
		if start_index < 1 then
			start_index = 1
		end
		self:save(start_index, index)
		-- print(tostring(start_index) .. ':' .. tostring(index))
	end
	self.events = {}
end

function Logger:save(start_index, stop_index)
	local file_path = self.file_folder .. self.file_name_prefix .. string.format('%08d', self.file_count) .. self.file_ext
	local csv_file = CSVFile:new(self.errors)
	
	csv_file:write_data_set_chunk(self.data_set, {}, start_index, stop_index, file_path, self.log_file_format)
	
	self.file_count = self.file_count + 1
end