callStack = [] # create an explicit call stack which is a dictionary

callStack.append([{'returnAddr':'start', 'number':5}])
returnValue = None

while len(callStack > 0):
    #body of the factorial() function

    number=callStack[-1]['number']

    returnAddr = callStack[-1]['returnAddr']

    if returnAddr == 'start':
        if number == 1:
            returnValue=1
            callStack.pop() 
            continue
        else:
            