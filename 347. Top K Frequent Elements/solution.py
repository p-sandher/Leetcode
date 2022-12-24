'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        MyDict = {}
        for num in nums:
            if (num not in MyDict):
                MyDict[num] = 1
            else:
                MyDict[num]+=1
        result = sorted(MyDict.items(), key=lambda d: d[1],reverse=True)
        resultList = []
        for i in range(0,k):
            resultList.append(result[i][0])
        return resultList
