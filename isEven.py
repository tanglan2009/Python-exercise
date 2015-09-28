


#Write a short Python function, is even(k), that takes an integer value and returns
# True if k is even, and False otherwise. However, your function cannot
# use the multiplication, modulo, or division operators.

def isEven(k):
    '''
    k: an integer value.
    return: True if k is even and False otherwise.
    '''

    if k == 0:
        return True
    if k == 1:
        return False

    if k > 0:
        return isEven(k-2)


print isEven(24)