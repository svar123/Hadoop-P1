#!/usr/bin/python
'''
Read in and outpute node-id and list of abs-parent-ids.
'''

import sys

for line in sys.stdin:
       data = line.strip().split("\t")
       print "{0}\t{1}".format(data[0],data[1])

         
    

