def isPrime(x):
    for i in range(2, x):
        if x%i ==0:
            return False
    return True

def primesList(N):
    """
    N: an integer
    Returns a list of prime numbers

    """
    primeL = []
    for i in range(2, N + 1):
        if isPrime(i):
            primeL.append(i)
            primeL.sort()
    return primeL
