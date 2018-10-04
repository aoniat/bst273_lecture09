#!/usr/bin/env python

import argparse
import sys

files= sys.argv[1]
parser = argparse.ArgumentParser( description="" )

parser.add_argument(
	"data_file",
	help="path to the file we want to read")

#-------------------------------------------------------------------------------
# Are there other arguments we need?
#-------------------------------------------------------------------------------

args = parser.parse_args( )
print(args)
print(args.data_file)

fh= open(args.data_file) #want to assign opening to
print("the file handle is", fh)

lines= 0 #want to return a number so set the lists to zero
words= 0
chars= 0
#-------------------------------------------------------------------------------
# our code for analyzing the data
#-------------------------------------------------------------------------------
for line in fh:
	print(line)
