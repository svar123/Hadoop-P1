#!/usr/bin/python

''' Read in a forum post and find the list of students that have posted in the answer/comment section for the question.'''

import sys

ques_dict = {}

for line in sys.stdin:
     data = line.strip().split("\t")
     id1,_,_,author_id,_,node_type,_,abs_parent_id,_,_,_,_,_,_,_,_,_,_,_ = data
     
     if id1 not in ques_dict and node_type == '"question"':
       ques_dict[id1] = [author_id]
     elif author_id not in ques_dict.values() and node_type == '"question"':
       ques_dict[id1].append(author_id)
     if node_type == '"answer"' or node_type == '"comment"':
       if abs_parent_id not in ques_dict.keys():
            ques_dict[abs_parent_id] = [author_id]
       else:
            ques_dict[abs_parent_id].append(author_id)
  
       

for keys in ques_dict.keys():           
       print "{0}\t{1}".format(keys,ques_dict[keys])
          
   
   

 
