def sumPowersOf2(power):
    result = 1
    if power == 0:
        return 1
    for i in range(power):
        result *= 2

    return result

print(sumPowersOf2(5))

def sumPowersOf2Recursive(power):
    if power == 0:
        return 1
    else:
        return 2 * sumPowersOf2Recursive(power-1)

print("The recursive version gives: ",sumPowersOf2Recursive(5))