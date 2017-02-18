import os.path
import re
from converter import *

def is_valid_file(parser, data_file):
	if not os.path.exists(data_file):
		parser.error("The file %s does not exist!" % arg)
	else:
		return data_file

def is_format_supported(parser,output_format):	
	if(output_format not in supported_format_method):
		return parser.error("The format %s is not supported yet!" % output_format)
	else:
		return output_format
		
def find_valid_data(data):
	return [object for object in data if object.data_is_valid()]