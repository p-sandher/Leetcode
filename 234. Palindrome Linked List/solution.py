# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def isPalindrome(self, head):
        if not head or not head.next : return True

        slow = head
        fast = head.next
        revStack = [slow.val]
        
        while fast.next and fast.next.next :
            fast = fast.next.next
            slow = slow.next
            revStack.append(slow.val)

        #Even or odd len handling 
        if not fast.next :
            second = slow.next
        else : 
            second = slow.next.next
        
        #Go through second half of the string and compare it with the first half that is reversed(popped from stack)
        while revStack :
            temp = revStack.pop()
            if temp != second.val :
                return False
            else :
                second = second.next
        return True

