#!/usr/bin/env python

import sys

#print "hello"

for line in sys.stdin:
    #print line
    data = line.strip().split("\t")
    if len(data)==2:
    	print data[0],"\t",data[1]	
	

