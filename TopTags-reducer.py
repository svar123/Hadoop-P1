#!/usr/bin/python
'''
Read in the tags and output the top ten.
'''

import sys
#from collections import OrderedDict
words_list=[]
words_dict={}

count = 0
for line in sys.stdin:
       data = line.strip()       
       if data not in words_dict:
          words_dict[data] = 1
       else:
          words_dict[data] +=1
words_lst = sorted(words_dict,key=words_dict.__getitem__,reverse=True)
for value in words_lst:
     print "{0}\t{1}".format(value,words_dict[value])
     count +=1
     if count == 10:
       break
         
    

