FileLinesIterator = {}

function FileLinesIterator:new(errors)
	newObj = {
		errors = errors,
		file = RWFile:new(errors),
		eof = false,
		line = nil
	}
	self.__index = self
	return setmetatable(newObj, self)
end

function FileLinesIterator:read_line()
	self.line = self.file:read_line()
	if self.line == nil then
		self.eof = true
	end 
end

function FileLinesIterator:open_file(file_path)
	self.file:open_file(file_path, 'r')
	if self.errors.error_occured then
		self.eof = true
	else
		self:read_line()
	end
end

function FileLinesIterator:close_file()
	self.file:close_file()
end

function FileLinesIterator:next_line()
	local line = self.line
	self:read_line()
	return line
end
