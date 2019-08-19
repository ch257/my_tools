dofile(script_file_folder .. "modules\\lua\\common\\Errors_1_0.lua")
dofile(script_file_folder .. "modules\\lua\\common\\RWFile_1_0.lua")
dofile(script_file_folder .. "modules\\lua\\common\\FileLinesIterator_1_0.lua")
dofile(script_file_folder .. "modules\\lua\\common\\RWini_1_0.lua")
dofile(script_file_folder .. "modules\\lua\\common\\StringTools_1_0.lua")
dofile(script_file_folder .. "modules\\lua\\common\\CSVFile_2_0.lua")
dofile(script_file_folder .. "modules\\lua\\common\\DataSetIterator_2_0.lua")
dofile(script_file_folder .. "modules\\lua\\common\\DataSetTools_2_0.lua")
dofile(script_file_folder .. "modules\\lua\\common\\FS_1_0.lua")
dofile(script_file_folder .. "modules\\lua\\common\\Logger_2_0.lua")

Template = {}

function Template:new()
	newObj = {
		errors = Errors:new(),
		settings = {}
	}
	self.__index = self
	return setmetatable(newObj, self)
end

function Template:read_settings(arguments)
	local rw_ini = RWini:new(self.errors)
	for i = 1, #arguments do
		local ini_file_path = script_file_folder .. "..\\" .. arguments[i]
		rw_ini:read_settings(ini_file_path)
	end

	rw_ini:copy_settings(rw_ini.settings, self.settings, nil)
	rw_ini:compose_settings(self.settings)
	
	-- rw_ini:print_settings(self.settings)
end

function Template:main(arguments)
	self:read_settings(arguments)
	-- if self.errors.error_occured  then
		-- self.errors:print_errors()
		-- return false
	-- end
	
	local input_file_path = self.settings['files']['input_file_folder'] .. self.settings['files']['input_file_name']
	local input_file_format = self.settings['files']['input_file_format']
	local output_file_path = self.settings['files']['output_file_folder'] .. self.settings['files']['output_file_name']
	local output_file_format = self.settings['files']['output_file_format']
	local log_settings = self.settings['log']
	local logger = Logger:new(self.errors, log_settings)
	
	local csv_file = CSVFile:new(self.errors)
	local ds_tools = DataSetTools:new(self.errors)
	
	local data_set = csv_file:read_data_set(input_file_path, input_file_format)
	local rec = {}
	
	ds_tools:add_columns(data_set, {'<ZZ1>', '<ZZ2>'}, {'num', 'num'})
	local add_cols_rec = {}
	
	local ds_iterator = DataSetIterator:new(self.errors, data_set)
	while not ds_iterator.eods do
		rec = ds_iterator:next_row()
		
		if ds_iterator.row_count % 2 == 0 then
			add_cols_rec['<ZZ1>'] = 100 + ds_iterator.row_count
			add_cols_rec['<ZZ2>'] = nil
		else
			add_cols_rec['<ZZ1>'] = nil
			add_cols_rec['<ZZ2>'] = 100 + ds_iterator.row_count
		end
		
		local close = rec['<CLOSE>']
		
		ds_tools:update_row(data_set, add_cols_rec, {'<ZZ1>', '<ZZ2>'}, ds_iterator.row_count)
		
		if ds_iterator.row_count % 10 == 0 then
			logger:add_event(ds_iterator.row_count)
		end
		logger:auto_save(ds_iterator.row_count)
	end
	
	-- csv_file:print_data_set(data_set, {'<DATE>', '<TIME>', '<ZZ1>', '<ZZ2>'}, output_file_format)
	csv_file:write_data_set(data_set, {}, output_file_path, output_file_format)
	
	
	if self.errors.error_occured  then
		self.errors:print_errors()
		return false
	end
	
	return true
end