# 
    # runtime: O(m+n)
    # memory: O(m+n)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        type l1: ListNode
        type l2: ListNode
        rtype: ListNode
        """
        head = ListNode(None)
        curr = head
        while l1!=None or l2!=None:
            if l1==None:
                curr.next = l2
                return head.next
            elif l2==None:
                curr.next = l1
                return head.next
            elif l1.val>l2.val:
                curr.next = l2
                l2 = l2.next
                curr = curr.next
            else:
                curr.next = l1
                l1 = l1.next
                curr = curr.next
        return head.next