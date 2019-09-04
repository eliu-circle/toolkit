#!/usr/bin/env python3

#########################################################################
## Modify each line in a file according to a given rule and output    ###
## Rule is defined in change_content function                         ###
##                                                                    ###
## Usage: python file_formatter.py INPUT_FILE_PATH OUTPUT_FILE_PATH   ###
#########################################################################

import sys
import os
import random

num = 100

def get_header():
	return "addressNumber, address, userName, privKey, disabled"

def get_address_number():
	global num
	num += 1
	return num

def get_user_name():
	names = ["mboorstin+polostg@circle.com", "eliu@circle.com", "jmayeux@circle.com"]	
	index = random.randint(0,2)
	return names[index]

def get_disabled():
	return 0	

def change_content(line):
	"""
	(these are fake data)
	
	Input file format :

	rPc2NgMjocQyPya8oTPZtzgkFLzoQsLDab : ssyGLDu2812MeSLjcmjkHrWRHgtab
	rng57VPZeFUHKvwLDg1JutJkkcjw9Uq4CD : snr3eLfZCwz8iJoCSx7a29387WmCD
	...

	Output file format:

	addressNumber, address, userName, privKey, disabled
	101, rPc2NgMjocQyPya8oTPZtzgkFLzoQsLDab, e@circle.com, ssyGLDu2812MeSLjcmjkHrWRHgtab, 0
	102, rng57VPZeFUHKvwLDg1JutJkkcjw9Uq4CD, e@circle.com, snr3eLfZCwz8iJoCSx7a29387WmCD, 0
	... 

	"""
	line = line.rstrip("\n")
	fields = line.split(" : ")
	addressNumber = get_address_number()
	address = fields[0]
	userName = get_user_name()
	privKey = fields[1]
	disabled = get_disabled()

	return "\n%s, %s, %s, %s, %s" % (addressNumber, address, userName, privKey, disabled)

def main():
	mode = 'a'

	input_path = sys.argv[1]
	output_path = sys.argv[2]

	if not os.path.isfile(input_path):
		print("INPUT FILE path {} does not exist. Exiting... ".format(input_path))

	if os.path.isfile(output_path):
		print("OUTPUT FILE path {} already exist. ".format(output_path))	
		do_delete = raw_input("Do you want to delete it? [y/n]")
		if do_delete.lower() == 'y':
			mode = 'w'
		else:
			print("Delete it first. Exiting ...")	
			exit()


	line_count = 0

	try:
		with open(input_path) as file_in:
			with open(output_path, mode) as file_out:
				file_out.write(get_header())

				for line in file_in:
					# line = file_in.readline()
					output_line = change_content(line)
					file_out.write(output_line)
					line_count += 1
	finally:
		file_in.close()
		file_out.close()

	print("Job done. {} lines".format(line_count))	

if __name__ == "__main__":
	main()