function findSubstringIterative(needle, haystack) {
    let i = 0;
    while (i < haystack.length) {
        if (haystack.substring(i, i+needle.length)==needle) {
            return i; //needle found
        }
        i = i + 1
    }
    return -1 //needle not found
}


function findSubstringRecursive(needle, haystack, i) {
    if (i===undefined) {
        i = 0;
    }
    if (i >= haystack.length) {
        return -1 //needle not found
    }

    if (haystack.substring(i,i+needle.length)==needle) {
        return i; //needle found
    }else {
        return findSubstringRecursive(needle, haystack, i+1)
    }
}