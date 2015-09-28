def isEven(n):

    if n == 0:
        return True
    if n == 1:
        return False

    if n > 0:
        return isEven(n-2)


print isEven(24)