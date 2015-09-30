# Write a short Python function that takes a positive integer n
# and returns the sum of the squares of all the positive integers
# smaller than n.

def sumSquares(n):
    '''
    n: a positive integer.
    return: the sum of the squares of all the positive integers
        smaller than n.
    '''

    sum = 0
    for i in range(1, n):
        sum += i*i
    return sum


# print sumSquares(12)

# Give a single command that computes the sum from above, relying on
# Python's comprehension syntax and the build-in sum function.

#total = sum(i*i for i in range(1, n))
def sumSquares2(n):
    total = sum(i*i for i in range(1, n))
    return total

# print sumSquares2(12)

# Write a short Python function that takes a positive integer n
# and returns the sum of the squares of all the odd positive
# integers smaller than n.

def sumOddSquares(n):
    sum = 0
    for i in range(n):
        if i%2 != 0:
            sum += i * i
    return sum

print sumOddSquares(21)


def sumOddSquares2(n):
    oddTotal = sum(i*i for i in range(1, n) if i%2 != 0)
    return oddTotal
print sumOddSquares2(21)










