def factorial(number):
    product = 1
    #base case
    if number == 1:
        return 1
    else:
        return number * factorial(number-1)

print(factorial(5))