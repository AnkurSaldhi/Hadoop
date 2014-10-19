#!/usr/bin/env python

import sys
def mapper():
	Totalnum=0
	Totalsales=0.0
	for line in sys.stdin:
		data = line.strip().split('\t')
		if len(data)==6:
			date,time,store,item,cost,payment=data
			Totalsales+=float(cost)
		Totalnum+=1
	print Totalnum,"\t",Totalsales
mapper()
