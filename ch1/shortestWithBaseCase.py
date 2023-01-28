def shortestWithBaseCase(makeRecursiveCall):
    print('shortestWithBaseCase(%s) called.'%makeRecursiveCall)
    if not makeRecursiveCall:
        #BASECASE
        print('Returning from base case')
        return
    else:
        #Recursive case
        shortestWithBaseCase(False)
        print('Returning from recursive call')
        return

print('Calling shortestWithBaseCase(False):')

shortestWithBaseCase(False)
print()
print('Calling shortestWithBaseCase(True)')
shortestWithBaseCase(True)