#The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

#Input: nums = [1,7,3,6,5,6]
#Output: 3


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        
        leftSum = 0
        for i in range(len(nums)):
            rightSum = total - nums[i] - leftSum
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        return -1               
