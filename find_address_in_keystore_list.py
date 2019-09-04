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

def get_keystore_dict(path):
	result = {}
	with open(path) as file:
		for line in file:
			line = line.rstrip("\n")
			[zone, time, address] = line.split("--")
			result[address] = "%s--%s" % (zone, time)
	file.close()
	return result

def get_address_list(path):
	result = []
	with open(path) as file:
		for line in file:
			line = line.rstrip("\n")
			address = line[2:]
			result.append(address)
	file.close()
	return result


def main():
	mode = 'a'
	keystore_list_path = sys.argv[1]
	address_list_path  = sys.argv[2]
	output_path  	   = "./result.out"

	if not os.path.isfile(keystore_list_path):
		print("INPUT FILE path {} does not exist. Exiting... ".format(keystore_list_path))

	if not os.path.isfile(address_list_path):
		print("INPUT FILE path {} does not exist. Exiting... ".format(address_list_path))		

	if os.path.isfile(output_path):
		print("OUTPUT FILE path {} already exist. ".format(output_path))	
		do_delete = raw_input("Do you want to delete it? [y/n]")
		if do_delete.lower() == 'y':
			mode = 'w'
		else:
			print("Delete it first. Exiting ...")	
			exit()

	total_address_count = 0
	success_count = 0
	missing_count = 0

	keystore_dict = get_keystore_dict(keystore_list_path)
	address_list = get_address_list(address_list_path)

	with open(output_path, mode) as file_out:
		for address in address_list:
			total_address_count += 1
			if address in keystore_dict:
				out_line = "\n%s--%s" % (keystore_dict[address], address)
				file_out.write(out_line)
				success_count += 1
			else:
				print("address %s not in keystore dict" % address)
				missing_count += 1
	file_out.close()

	print("Job done. {} addresses input. {} found, {} missing in keystore file {}".format(total_address_count, success_count, missing_count, keystore_list_path))	

if __name__ == "__main__":
	main()