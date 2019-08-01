script_file_folder = arg[0]:match('.*\\')

dofile(script_file_folder .. "modules\\lua\\Template.lua")

local template = Template:new()
if template:main(arg) then
	print("OK\n")
else
	print("Error\n")
end
