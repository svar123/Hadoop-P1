#!/usr/bin/python
'''
Read in the length of the question and avg length of answer and print it.
'''

import sys

for line in sys.stdin:
       data = line.strip().split("\t")
       print "{0}\t{1}\t{2}".format(data[0],data[1],data[2])

         
    

