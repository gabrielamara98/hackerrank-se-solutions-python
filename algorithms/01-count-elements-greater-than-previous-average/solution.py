def countResponseTimeRegressions(responseTimes):
    ## Edge Case
    if len(responseTimes) < 2:
        return 0
    
    average = responseTimes[0]
    count = 0
    for x in range(1,len(responseTimes)):
        if responseTimes[x] > (average/x):
            count +=1
        average+= responseTimes[x]        
    return count