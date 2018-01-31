#!/usr/bin/python

''' Read in a forum post and output authorid and hour fields'''

import sys

for line in sys.stdin:
     data = line.strip().split("\t")
     author = data[3]
     time = data[8]
     author = data[3][1:10]
     if len(time) > 14:
        time = data[8][12:14]
   
     print ( "{0}\t{1}".format(author,time))
 
