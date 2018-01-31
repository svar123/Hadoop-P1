#!/usr/bin/python
'''
Read in the authorid and hour. Calculate the hour during which the student has posted the most posts.
'''

import sys

auth_time_dict={} 
auth=[]

for line in sys.stdin:
       data = line.strip().split()
       author, time = data
    
       if (author,time) in auth_time_dict:
              auth_time_dict[author,time] += 1              
       else:
           auth_time_dict[author,time] = 1
       if author not in auth:
            auth.append(author)              

for item in auth:
    temp=[]
    max_val = 0
    for keys in auth_time_dict.keys():
        if keys[0] == item:
            val = auth_time_dict[keys]
            if val > max_val:
               max_val = val
               t = keys[1]
    for keys in auth_time_dict.keys():
        if keys[0] == item:
           if auth_time_dict[keys] == max_val:
              print "{0}\t{1}".format(item,keys[1])
    

