def processCouponStackOperations(operations):
    # Main stack responsible to append the elements
    stack=[]
    # Stack for the minimum numbers to keepthe record and manipulate 
    min_number = []
    # The final output of the function
    output = []
    for op in operations:
        if getPush(op,stack):
            # Checks if the min_number is not empty and compare with the recently pushed number by the function
            if len(min_number) > 0 and (stack[-1] <= min_number[-1]):
                min_number.append(stack[-1])
            # Append the last number of the stack if the list is empty (essential for the first number or empty stack )
            if len(min_number) < 1:
                min_number.append(stack[-1])
        elif getPop(op):
            # Checks if this is the minimum number so it can keep a updated record
            if stack[-1] == min_number[-1]:
                min_number.pop()
            stack.pop()
        elif getTop(op):
            output.append(stack[-1])
        elif getMin(op):
            output.append(min_number[-1])
    return output

## Auxiliary functions
def getPush(operation,stack):
    if operation[0] == 'p' and operation[1] == 'u':
        number = int(operation[5:])
        stack.append(number)
        return True
    return False

def getMin(operation):
    if operation == 'getMin':return True

def getPop(operation):
    if operation == 'pop':return True

def getTop(operation):
    if operation == 'top':return True