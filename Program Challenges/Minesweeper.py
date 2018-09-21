import sys
import functools
import os
class Mine:
    data = []
    width = 0
    height = 0
    def __int__(self):
        self.width = 0
        self.height = 0

#@functools.lru_cache(None)
def caluclateMines(mineList):
    for index, mine in enumerate(mineList):
        for i, lineValue in enumerate(mine.data):
            for j,value in enumerate(lineValue):
                if(value == '.'):
                    mineCount = 0
                    if(i > 0 and mine.data[i-1][j] == '*'):
                        mineCount = mineCount + 1
                    if(i < mine.width - 1 and mine.data[i+1][j] == '*'):
                        mineCount = mineCount + 1
                    if(j > 0 and mine.data[i][j-1] == '*'):
                        mineCount = mineCount + 1
                    if(j < mine.height - 1 and mine.data[i][j+1] == '*'):
                        mineCount = mineCount + 1
                    mine.data[i][j] = mineCount
        print ("Field #",index + 1,":")
        for lineValue in mine.data:
            print(''.join(str(i) for i in lineValue))
        print('\n')
    os._exit()

if __name__ == '__main__':
    currentMine = Mine()
    mineList = []        
    for line in sys.stdin:
        characters = line.split()
        if len(characters) == 2 and all(str.isnumeric(i) for i in characters):
            width, height = map(int,characters[:2])
            if(width == 0 and height == 0):
                if currentMine.width > 0 and currentMine.height > 0:
                    mineList.append(currentMine)
                caluclateMines(mineList)
            elif currentMine.width > 0 and currentMine.height > 0:
                mineList.append(currentMine)
                currentMine = Mine()
                currentMine.data = []
            currentMine.width = width
            currentMine.height = height
        else:
            splitedLine = list(line)
            currentMine.data.append(splitedLine[:-1])
    exit(0)