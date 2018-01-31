#!/usr/bin/python

''' Read in a forum post and output id, node_type, body and abs_parent_id fields.
Find the length of question and avg length of answer.'''

import sys
import math

ques_dict = {}
ans_dict = {}
for line in sys.stdin:
     data = line.strip().split("\t")
     id1,_,_,_,body,node_type,_,abs_parent_id,_,_,_,_,_,_,_,_,_,_,_ = data
     
   

     
     if id1 not in ques_dict and node_type == '"question"':
       ques_dict[id1] = len(body)-2
     if abs_parent_id not in ans_dict and node_type == '"answer"':
       ans_dict[abs_parent_id] = [len(body)-2]
     elif abs_parent_id in ans_dict and node_type == '"answer"':
       ans_dict[abs_parent_id].append(len(body)-2)
       

for keys in ques_dict.keys():
    avg_val=0
    for keys_ans in ans_dict.keys():
          if keys_ans == keys:              
             avg_val = float (sum(ans_dict[keys_ans])/len(ans_dict[keys_ans]))
    print "{0}\t{1}\t{2}".format(keys,ques_dict[keys],avg_val)
          
   
   

 
