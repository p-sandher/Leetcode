class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
    #return true if any value appears at least twice in the array, and return false if every element is distinct.
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False 

#hashset value is array element, if its found, return True
