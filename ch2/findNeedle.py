exString = "This is an example string to see if this works. Let's see if this thing can find a needle in a haystack"

def findNeedleInter(str):
    wordsInString = str.split()
    for i in range(len(wordsInString)):
        if wordsInString[i] == "needle":
            print(f'Found the word: {wordsInString[i]} at position {i}.')
            return i
        else:
            continue
    return -1

findNeedleInter(exString)

def findNeedleRecur(needle, haystack, i=0):
    wordsInStr = haystack.split()
    if wordsInStr[i] == needle:
        print(f"Found the needle: {needle} at index: {i}")
        return 0
    elif len(wordsInStr) >= i:
        print(f"Still looking for {needle}.")
        return findNeedleRecur(needle, haystack, i + 1)
    else:
        print("No needle found.")
        return -1

findNeedleRecur("string", exString, i = 0)


