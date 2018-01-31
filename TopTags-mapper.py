#!/usr/bin/python

''' Read in a forum post,and output the tags if node-type is "question".'''

import sys
from collections import OrderedDict
count={}


for line in sys.stdin:
     data = line.strip().split("\t")
     _,_,tags,_,_,node_type,_,_,_,_,_,_,_,_,_,_,_,_,_ = data
     tags_lst = tags.split()
     if node_type == '"question"':
         for items in tags_lst:
             items = items.replace('"','')
             print "{0}".format(items)


          
   
   

 
