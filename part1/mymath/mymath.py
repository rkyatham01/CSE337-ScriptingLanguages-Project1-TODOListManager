import random as rd

def isPrime(n): #sqrt of n algo O(sqrt(n))
    for i in range(2, int(n**(0.5))+1): # we do up to sqrt(n) b/c this is where it
        #breaks out the cofactors to the left and the right would be all factors
        if n % i == 0:
            return False
    return True

def gcd(a,b):
    #base case
    #Used Euclideans theorem
    if b == 0: #if remainder is 0, then return the a which is the GCD
        return a 
    return gcd(b,a%b) #b is the factor and a % b is the remainder
    #pass in (factor, remainder)

def lcm(a,b): 
    return (a * b) // gcd(a,b) #gets the lcm 
    #from the formula gcd(a,b) * lcm(a,b) = a * b

# Generates public key exponent
def pubkExp(k): #used to encrypt (for everyones use)
    e = rd.randint(2,k-1) #generates a random number within
    while gcd(e,k) != 1:
        e = rd.randint(2,k-1) #generates a random number within

    return e

# Generate private key exponent 
def prikExp(x, y): #used to decrypt (for private use) 
    #used modular multiplicative inverse
    if x > y:
        x, y = y, x

    for i in range(1, y):
        num = (y*i) + 1
        if not num % x:
            return (num) // x
    return -1

# Returns the hash of a string message. Sum of its ascii characters.
def hash(s):
    Sum = 0
    for i in s:
        Sum += ord(i)
    return Sum

def modularExponetion(a,b,c):
    x = 1
    while(b > 0):
        num = b & 1
        if(num == 1): 
            mult = x*a
            x = mult % c #set x here
        powr = a**2
        a = powr % c
        b >>= 1 #bit shift by 1
    return x % c