#Given an integer n, return true if it is a power of five. Otherwise, return false.

def isPowerOfFive(n):
    if n <= 0:
        return False
    while n % 5 == 0:
        n //= 5
    return n == 1

                               
print(isPowerOfFive(17))       
print(isPowerOfFive(125))     