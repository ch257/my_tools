FS = {}

function FS:new(errors)
	newObj = {
		errors = errors
	}
	self.__index = self
	return setmetatable(newObj, self)
end

function FS:clear_folder(folder_path)
	if folder_path ~= nil and folder_path ~= '' then
		local i, popen = 0, io.popen
		for fname in popen('dir "'.. folder_path ..'" /b'):lines() do
			local f = io.open(folder_path .. fname)
			if f then
				f:close()
				res = os.execute('del /q ' .. folder_path .. fname)
			else
				res = os.execute('rd /q/s ' .. folder_path .. fname)
			end
		
			if not res then
				self.errors:raise_error('critical', 'Can\'t clear folder ' .. folder_path)
				return nil
			end
		end
	else 
		self.errors:raise_error('critical', 'Folder path is empty')
	end
end