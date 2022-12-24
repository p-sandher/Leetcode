'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # collection of defaultdict that counts and stores char count
        dictionary = collections.defaultdict(list)
        for word in strs:
            # tuple allows storage of multiple items
            #all sorted words are the same which collects them together 
            dictionary[tuple(sorted(word))].append(word)
        #list returns it as a sorted list object
        return list(dictionary.values())
