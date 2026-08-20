def findSmallestMissingPositive(orderNumbers):
    ##Place each positive number at target index(n -> index n - 1)
    x = 0
    while x < len(orderNumbers):
        element = orderNumbers[x]
        ##Handle Edge cases
        if (element > 0) and (element <= len(orderNumbers)) and (element!= orderNumbers[element-1]) : 
            orderNumbers[x], orderNumbers[element-1] = orderNumbers[element-1],orderNumbers[x]
        else:
            x = x + 1
    ##Check if a number is missing from the index (i + 1)
    for i in range(len(orderNumbers)):
        if(orderNumbers[i] != i+1 ):
            return i + 1
    return len(orderNumbers) + 1