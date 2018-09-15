# -*- coding: utf-8 -*-
"""
Created on Thu May 31 07:17:21 2018

@author: alan.jin
"""

cities = input('please input your cities').split()
distances = list(map(int, cities))
cityCount = len(distances) + 1
for i in range(cityCount):
    for j in range(cityCount):
        if(i == j):
            print(0, end=' ')
        else:
            s = i;
            e = j;
            if(i > j):
                s = j;
                e = i;
            distance = 0;
            for k in range(s,e):
                distance = distance + distances[k]
            print (distance, end=' ')
    print ('\n')
