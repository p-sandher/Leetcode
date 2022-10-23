class Solution:
    def romanToInt(self, s: str) -> int:
        length = len(s)
        num = 0
        
       
        for x in s:
            if(x == 'I'):
                num+=1
            elif(x == 'V'):
                num+=5
            elif(x == 'X'):
                num+=10
            elif(x == 'L'):
                num+=50
            elif(x == 'C'):
                num+=100
            elif(x == 'D'):
                num+=500
            elif(x == 'M'):
                num+=1000
        return num
