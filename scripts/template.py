# -*- coding: utf-8 -*

import sys
from os.path import dirname
from os.path import abspath

script_file_folder = abspath(dirname(sys.argv[0])) + '\\'
MY_TOOLS_MODULES_FOLDER = script_file_folder + 'modules\\python'
sys.path.insert(0, MY_TOOLS_MODULES_FOLDER)

from modules.python.Template import *

template = Template()
if template.main(sys.argv):
	print("OK\n")
else:
	print("Error\n")