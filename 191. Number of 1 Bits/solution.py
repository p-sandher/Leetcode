class Solution:
    def hammingWeight(self, n: int) -> int:
        #counter number of 1 bits, unsigned doesnt really matter
        
        res = 0
        while n:  
            #while n isnt 0
            res+= n%2
            n = n >> 1
            #bit shift operation moves it to the right, same as /2
        return res
    
    #its a 32bit integer
    #therefore O(1)
