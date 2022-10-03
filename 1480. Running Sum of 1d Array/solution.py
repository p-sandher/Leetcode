class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1] #replace each value in array with new added value
        return nums
#sorta like fibonacci for one term
