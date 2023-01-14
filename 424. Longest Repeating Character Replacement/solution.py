class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ''' 
        You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

        Input: s = "ABAB", k = 2
        Output: 4
        Explanation: Replace the two 'A's with two 'B's or vice versa.
        '''


        # Sliding window problem
        countChar = {}
        res = 0

        left = 0

        for right in range(len(s)):
            #get char from right index in s
            #find that char and add 1, if its not there then default 0
            countChar[s[right]] = 1 + countChar.get(s[right], 0)
            
            #max values from charCounter
            while (right - left + 1) - max(countChar.values()) > k:
                countChar[s[left]] -= 1

                left+=1

            res = max(res, right - left + 1)
        return res
