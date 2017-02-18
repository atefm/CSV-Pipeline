import argparse,sys,csv
from validate import *
import re
from hotel import *

def check_arg(args=None):
    parser = argparse.ArgumentParser(description='CSV Parser')
    parser.add_argument('-i', '--input',
                        help='Input CSV file',
                        required='True', metavar = "input", type = lambda data: is_valid_file(parser, data))
    parser.add_argument('-f', '--format',
                        help='Output format',
                        default='html',metavar="FORMAT", type= lambda output_format: is_format_supported(parser,output_format))

    results = parser.parse_args(args)
    return (results.input,results.format)
	
def readData(file_name):
	csvFile = open(data_file)
	csvReader = csv.reader(csvFile)
	csvData = list(csvReader)
	
	return csvData

def convertToHotels(data):
	hotels = []
	for rowIndex in range(1, len(data)):
		row = data[rowIndex]
		hotels.append(Hotel(row))
	return hotels
	
def save(data_file,output_format,data):
	data_file=data_file.split('.')
	obj = open(data_file[0]+'.'+output_format, 'w')
	obj.write(data)
	obj.close


if __name__ == '__main__':
	data_file, output_format= check_arg(sys.argv[1:])
	data = readData(data_file)
	hotels = convertToHotels(data)
	valid_hotels = find_valid_data(hotels)
		
	output = supported_format_method[output_format](valid_hotels)
	save(data_file,output_format,output)
