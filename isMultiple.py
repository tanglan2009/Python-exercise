 # Write a short Python function, isMultiple(n, m), that takes two integer
 # values and returns True if n is a multiple of m, that is n = mi
 # for some integer i, and False otherwis.

def isMultiple(n, m):
     '''
     n, m: two integer values.
     return: True if n is a multiple of m, and False otherwise.
     '''
     if n % m == 0:
         return True
     else:
        return False



print isMultiple(15, 3)