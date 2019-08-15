# -*- coding: utf-8 -*

import re
import sys

script_file_folder = (re.match(".*\\\\", sys.argv[0])).group(0)

from modules.python.Template import *

template = Template()
if template.main(sys.argv):
	print("OK\n")
else:
	print("Error\n")