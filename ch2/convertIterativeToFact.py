def interativeFunction(n):
    for i in range(n):
        print("Iterating through")

interativeFunction(10)
print()

#convert this to a factorial problem
def factorialFunction(n):
    if n == 1:
        print("Base case", n)
        return 0
    else:
        print("Not the base case", n)
        return factorialFunction(n-1)

def factorialFunctionTwo(n):
    if n == 1:
        print('Base case: ', n)
        return 0
    while (n > 1):
        print("Not the base case: ", n)
        return factorialFunctionTwo(n-1)


factorialFunction(10)
print()
factorialFunctionTwo(10)