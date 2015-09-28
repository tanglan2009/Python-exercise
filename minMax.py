# Write a short Python function, minmax(data), that takes a sequence of one or more numbers,
# and returns the smallest and largest numbers, in the form of a tuple of length two. Do not
# use the built-in functions min or mas in implementing your solution.

def minMax(data):
    '''
    data: a sequence of one or more numbers.
    return: the smallest and largest numbers in the form of a tuple of length two.
    '''
    smallest = None
    largest = None
    t = ()
    for i in data:
        if smallest is None or i < smallest:
            smallest = i
            print smallest
        if largest is None or i > largest:
            largest = i
            print largest
    t = (smallest, largest)
    return t


print minMax([3, 41, 12, 9, 74, 15])

