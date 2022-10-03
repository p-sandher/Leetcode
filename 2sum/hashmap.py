class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} #empty hash map value:index
        
        for i, n in enumerate(nums): 
            #i gives the count of the iteration
            #n is the item at the current iteration
            diff = target - n
            if diff in prevMap: #if difference is a value in the hashmap
                return [prevMap[diff], i]
            prevMap[n] = i #if not, add that value into the hashmap
        return
