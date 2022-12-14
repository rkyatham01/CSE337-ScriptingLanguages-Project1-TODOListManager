import random as rd
import mymath.mymath as maths
# import the mymath module here.

class Rsa:
    # initialize to set p, q, and n.
    def __init__(self,x): #get an x value
        
        self.p = rd.randint(x,x+1000)
        while (maths.isPrime(self.p) == False):
            self.p = rd.randint(x,x+1000)
        #when its true , self.p is prime
        
        self.q = rd.randint(x, x+1000)

        while (maths.isPrime(self.q) == False and self.q != self.p):
            self.q = rd.randint(x,x+1000)   
        self.n = self.p*self.q

    # generates a cipher string for a message m
    def encrypt(self, sumOfAscii):
        K = maths.lcm(self.p-1, self.q-1) #step 2
        e = maths.pubkExp(K) #e is the public key
        #then use moduluar exponentiation 
        d = maths.modularExponetion(sumOfAscii, e, self.n) 
        #gets the modular Exponention 
        #passing in the tuple
        return (d, e)
        
    # decrypts a cipher string to get back original message
    def decrypt(self, c, e):
        K = maths.lcm(self.p-1, self.q-1) 
        d = maths.prikExp(e,K) #you pass in K and public key
        m = maths.modularExponetion(c, d, self.n)
        return m


