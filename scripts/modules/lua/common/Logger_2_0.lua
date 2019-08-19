Logger = {}

function Logger:new(errors, settings)
	newObj = {
		errors = errors,
		settings = settings,
		events = {}
		-- log_file = RWFile:new(errors),
		-- tools = Tools:new(errors),
		-- fs = FS:new(errors),
		-- file_count = 1
	}
	self.__index = self
	return setmetatable(newObj, self)
end

-- function Logger:init(log_params, stream)
	-- if self.errors.critical_error_occured then
		-- return nil
	-- end
	-- self.log_files_folder = log_params['log_files_folder']
	-- self.logger_file_column_div = self.tools:escape_sequence(log_params['logger_file_column_div'])
	-- if log_params['add_header']:lower() == 'yes' or log_params['add_header']:lower() == 'y' then
		-- self.add_header = true
	-- end
	-- self.chunk_length = tonumber(log_params['chunk_length'])
	-- self.after_event_length = tonumber(log_params['after_event_length'])
	-- self.stream = stream
	-- self.fs:clear_folder(self.log_files_folder)
-- end

function Logger:add_event(index)
	table.insert(self.events, index)
end

-- function Logger:auto_save(index)
	-- local to_remove = {}
	-- local offset = 0
	-- for i = 1, #self.events do
		-- if index - self.events[i] >= self.after_event_length then
			-- self:save(index - self.chunk_length + 1, index)
			-- table.insert(to_remove, i - offset)
			-- offset = offset + 1
		-- end
	-- end
	-- for i = 1, #to_remove do
		-- table.remove(self.events, to_remove[i])
	-- end
-- end

-- function Logger:save_remained_events(index)
	-- for i = 1, #self.events do
		-- self:save(self.events[i] - (self.chunk_length - self.after_event_length) + 1, index)
	-- end
	-- self.events = {}
-- end

-- function Logger:save(start_index, stop_index)
	-- if start_index < 1 then
		-- start_index = 1
	-- end
	
	-- self.log_file:open_file(self.log_files_folder .. string.format('%#08d', self.file_count) .. '.txt', 'w')
	-- if self.add_header then	
		-- self.log_file:write_line(self.stream.output_file_header)
	-- end
	-- for index = start_index, stop_index do	
		-- local line = ''
		-- for i = 1, #self.stream.stream_format.stream_keys do
			-- line = line .. self.logger_file_column_div .. self.stream.series[self.stream.stream_format.stream_keys[i]][index]
		-- end
		-- self.log_file:write_line(string.sub(line, 2))
	-- end
	-- self.log_file:close_file()
	-- self.file_count = self.file_count + 1
-- end