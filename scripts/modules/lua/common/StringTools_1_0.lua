StringTools = {}

function StringTools:new(errors)
	newObj = {
		errors = errors
	}
	self.__index = self
	return setmetatable(newObj, self)
end

function StringTools:split(str, sep)
	items = {}
	sep_pos = string.find(str, sep)
	while sep_pos ~= nil do
		table.insert(items, string.sub(str, 1, sep_pos-1))
		str = string.sub(str, sep_pos + string.len(sep), -1)
		sep_pos = string.find(str, sep)
	end
	table.insert(items, str)
	return items
end

function StringTools:join(items, sep)
	str = ''
	for i = 1, #items do
		str = str .. items[i] .. sep
	end
	return string.sub(str, 1, -2)
end

