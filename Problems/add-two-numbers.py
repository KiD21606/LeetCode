# 
    # runtime: O(max(m,n))
    # memory: O(max(m,n))

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode(None)
        pointer = ans
        carry = 0
        
        while l1 or l2:
            summ = carry
            if l1:
                summ += l1.val
                l1 = l1.next
            if l2:
                summ += l2.val
                l2 = l2.next
            if summ>=10:
                carry = 1
                summ -= 10
            else:
                carry = 0
            pointer.next = ListNode(summ)
            pointer = pointer.next
        if carry:
            pointer.next = ListNode(1)
        return ans.next