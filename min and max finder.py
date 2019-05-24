testList = [0, 1, -3, 99, 101,23, 22]

def findMaxVal(testList):

    maximumVal = max(testList)
    return maximumVal

def findMinVal(testList):
    
    minimumVal = min(testList)
    return minimumVal

def main(testList):
    maxVal = findMaxVal(testList)
    minVal = findMinVal(testList)
    
    print('Maximum Value: ' , maxVal)
    print('Minimum Value: ' , minVal)

main(testList)