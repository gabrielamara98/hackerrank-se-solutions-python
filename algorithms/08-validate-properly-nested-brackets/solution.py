def areBracketsProperlyMatched(code_snippet):
    stack = []
    for letter in code_snippet:
        stack_top = ''
        if letter in '[{(':
            stack.append(letter)
        elif letter in ']})':
            if len(stack) == 0:
                return 0
            stack_top = stack.pop()
            if not checkBrackets(stack_top, letter):
                return 0
    if len(stack) > 0:
        return 0
    return 1
            
            
def checkBrackets(initial,end):
    if initial == '(' and end == ')': return True
    if initial == '{' and end == '}': return True
    if initial == '[' and end == ']': return True
    return False
