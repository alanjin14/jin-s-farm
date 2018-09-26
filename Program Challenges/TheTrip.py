import sys
import functools
import os
import math

class Trip:
    spend = []
    count = 0
    def __int__(self):
        self.count = 0

#@functools.lru_cache(None)
def caluclateTrips(tripList):
    for trip in tripList:
        posDiff = 0
        negDiff = 0
        average = sum(trip.spend)/len(trip.spend)
        lowerAverage=math.floor(average*100)/100  
        upperAverage=math.ceil(average*100)/100
        for spend in trip.spend:
            if (spend > average):
                posDiff = posDiff + spend - upperAverage
            
            else:
                negDiff = negDiff + lowerAverage - spend
        amount_exchanged=max(negDiff,posDiff)
        amount_exchanged=round(amount_exchanged,2)
        print ("${:.2f}".format(amount_exchanged))

if __name__ == '__main__':
    currentTrip = Trip()
    tripList = []        
    for line in sys.stdin:
        value = line.split()[0]
        if str.isnumeric(value):
            if(int(value) == 0):
                tripList.append(currentTrip)
                caluclateTrips(tripList)
                break
            elif currentTrip.count > 0:
                tripList.append(currentTrip)
                currentTrip = Trip()
                currentTrip.spend = []
            currentTrip.count = int(value)
        else:
            currentTrip.spend.append(float(value))
    exit(0)