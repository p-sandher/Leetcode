class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack = []
        intersect = []
        for n in nums1:
            stack.append(n)
        
        for i in nums1:
            num = stack.pop()
            if num in nums2:
                intersect.append(num)
                nums2.remove(num)
        return intersect
