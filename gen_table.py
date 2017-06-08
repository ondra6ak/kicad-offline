#!/usr/bin/python3
import sys
import argpar
import os

if __name__ == '__main__':
	args = argpar.parse({"t": sys.stdout}, sys.argv, posarg={"path": "./"})
	if type(args["t"]) == str:
		args["t"] = open(args["t"], "w")
	
	sys.argv.append(args["path"])

	print("(fp_lib_table", file=args["t"], flush=True)
	for directory in sys.argv[1:]:
		for lib in os.listdir(directory):
			if lib.endswith(".pretty"):
				print("  (lib (name {})(type KiCad)(uri {})(options \"\")(descr \"\"))".format(lib[:-7], os.path.abspath(lib)), file=args["t"], flush=True)
	print(")", file=args["t"], flush=True)
	args["t"].close()