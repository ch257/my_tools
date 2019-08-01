Errors = {}

function Errors:new()
	newObj = {
		errors = {},
		error_occured = false
	}
	self.__index = self
	return setmetatable(newObj, self)
end

function Errors:raise_error(desc)
	self.error_occured = true
	table.insert(self.errors, desc)
end

function Errors:print_errors()
	error_message = ''
	for i = 1, #self.errors do
		error_message = error_message .. self.errors[i] .. '\n'
	end
	print(error_message)
end