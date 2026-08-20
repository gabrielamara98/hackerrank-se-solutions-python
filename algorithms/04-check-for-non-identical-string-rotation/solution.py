def isNonTrivialRotation(s1, s2):
    ## Edge cases
    if len(s1) != len(s2) or s1 == s2:
        return 0
    n = 0    
    ## Check rotation using s1 and s2 inverse position
    while n < len(s1):
        s1_rotation = s1[n:] + s1[:n]
        if s1_rotation == s2:
            return 1
        n+=1
    return 0