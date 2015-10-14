# Write a Python function that returns a list of keys in aDict that map to integer
# values that are unique (i.e. values appear exactly once in aDict).
# The list of keys you return should be sorted in increasing order.
#  (If aDict does not contain any unique values, you should return an empty list.)
def uniqueValues(aDict):
    '''
    aDict a dictionary
    return a list of keys that map to values which appear exactly once in aDict.

    '''

    keyList = []
    valList = aDict.values()
    for key in aDict:
        val = aDict[key]
        if valList.count(val) == 1:
            keyList.append(key)
    keyList.sort()
    return keyList

# print uniqueValues({1: 1, 2: 2, 3: 3})
# print uniqueValues({1: 1, 2: 1, 3: 1})
# print uniqueValues({1: 1})
# print uniqueValues({1: 1, 2: 1, 3: 3})
