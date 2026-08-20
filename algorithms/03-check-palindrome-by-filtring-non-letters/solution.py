def isAlphabeticPalindrome(code):
    cd = ""
    ##Select and populate in a String only letters
    for x in code:
        if x.isalpha():
            x = x.lower()
            cd+=x
    palindrome_test = ""
    ##Reverse the cd to create a possible palindrome
    for n in range(len(cd)-1,-1,-1):
        palindrome_test += cd[n]
    ##Comparing cleaned code with reversed code(palindrome)
    if cd == palindrome_test:
        return 1
    else:
        return 0