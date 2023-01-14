'''
Given a string s, find the length of the longest 
substring
 without repeating characters.
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        left = 0
        maxString = 0

        for right in range(len(s)):
            # keep looping until you remove all the duplicates
            #remove from left (moving the pointer)
            #sliding door 
            while s[right] in chars:
                chars.remove(s[left])
                left+=1
            #add new char
            #recalculate max
            chars.add(s[right])
            maxString = max(maxString,right-left+1)
        return maxString
