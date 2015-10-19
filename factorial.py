def factorial(n):
    if n== 0:
        return 1
    else:
        return n * factorial (n-1)

print factorial(5)

def factorial(n):
    # use the build-in function isinstance to verify the type of the argument.
    if not isinstance(n, int):
        print 'Factorial is only defined for integers.'
        return None
    elif n < 0:
        print 'Factorial is not defined for negative integers.'
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)