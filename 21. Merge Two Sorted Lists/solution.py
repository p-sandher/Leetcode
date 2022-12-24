# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        newHead = ListNode(0)
        newL = newHead

        while l1 and l2:# if neither l1 nor l2 have finished
            if l1.val <= l2.val:
                newL.next = l1
                l1 = l1.next
            else:
                newL.next = l2
                l2 = l2.next
            newL = newL.next
        
        while l1:# if l2 has already finished
            newL.next = l1
            l1 = l1.next
            newL = newL.next
        while l2:# if l1 has already finished
            newL.next = l2
            l2 = l2.next
            newL = newL.next
        return newHead.next
        
