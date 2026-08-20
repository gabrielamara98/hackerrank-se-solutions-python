def maximizeNonOverlappingMeetings(meetings):
    ##Edge case
    if len(meetings) < 1:
        return None
    ##Sort the 2D list using the last element of each interval
    meetings.sort(key = lambda x: x[1])
    count = 1
    last_end = meetings[0][1]
    for x in range(1,len(meetings)): 
        if meetings[x][0] >= last_end:
            count +=1 
            last_end = meetings[x][1]
    return count
   