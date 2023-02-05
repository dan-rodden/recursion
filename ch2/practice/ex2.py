#we need to add the two previous numbers until we have reached n
#problem is not initializing the result
def fibonacci(n):
    if n == 1 or n == 2:
        print("Reached base case")
        return 1
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
        print("The current result is: ",result)
        return result

print(fibonacci(10))

