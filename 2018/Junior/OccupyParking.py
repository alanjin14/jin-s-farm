# -*- coding: utf-8 -*-
"""
Created on Wed May 30 08:27:36 2018

@author: alan.jin
"""

parkingNumber = int(input('Please input parking number: '))
yesterdayParking = input('Please input parking yesterday: ')
todayParking = input('Please input parking today: ')
same = 0
for i in range(parkingNumber):
    if yesterdayParking[i] == todayParking[i] == 'c':
        same = same + 1
print (same)