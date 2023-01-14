'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #map count of chars to a list of anagrams
        resMap = defaultdict(list)

        for s in strs:
            # an array from a-z, default 0
            count = [0] * 26

            for c in s:
                #get string, loop thorugh each char, and count
                count[ord(c) - ord("a")] +=1
            # key has to be tuple
            resMap[tuple(count)].append(s)
        return resMap.values()

