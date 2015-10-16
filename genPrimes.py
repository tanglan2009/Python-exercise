def genPrimes(x):
    for i in range(2, x + 1):
        if isPrime(i):
            yield i
def isPrime(x):
    for i in range(2, x):
        if x%i == 0:
            return False
    return True


print genPrimes(10)