def fibonacci(n):
    a,b = 1,1

    print('a=%s, b=%s'%(a,b))
    for i in range(1, n):
        a,b = b, a+b # get the next fibonacci number
        print('a=%s, b=%s'%(a,b))
    return a

print(fibonacci(10))

def recur_fibonacci(n):
    if n == 1 or n == 2:
        print("reached base case")
        return 1
    else:
        result = recur_fibonacci(n-1) + recur_fibonacci(n-2)
        print(result)
        return result

recur_fibonacci(10)


