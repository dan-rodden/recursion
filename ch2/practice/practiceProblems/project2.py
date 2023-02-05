def sumSeriesRec(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        result = n + sumSeriesRec(n-1)
        return result

print(sumSeriesRec(3))