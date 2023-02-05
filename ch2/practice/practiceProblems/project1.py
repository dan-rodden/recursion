def calcSum(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    count = 1
    result = 0
    while count <= n:
        result += count
        count += 1

    return result

print(calcSum(3))