RWFile = {}

function RWFile:new(errors)
	newObj = {
		file_handler = nil,
		errors = errors
	}
	self.__index = self
	return setmetatable(newObj, self)
end

function RWFile:open_file(file_path, mode)
	self.file_handler = io.open(file_path or '', mode or 'r')
	if self.file_handler == nil then
		self.errors:raise_error('Can\'t open file "' .. (file_path or '') .. '"')
	end
end

function RWFile:read_line()
	return self.file_handler:read("*l")
end

function RWFile:write_line(line)
	self.file_handler:write(line .. '\n')
end

function RWFile:close_file()
	if self.file_handler ~= nil then
		io.close(self.file_handler)
	end
end