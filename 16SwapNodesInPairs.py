# Question: https://leetcode.com/problems/swap-nodes-in-pairs/

# Solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        temp = dummy
        while temp.next and temp.next.next:
            first, second = temp.next, temp.next.next
            first.next = second.next
            temp.next = second
            temp.next.next = first
            temp = temp.next.next
        return dummy.next
      
# Verdict:
# Runtime: 54 ms, faster than 24.07% of Python3 online submissions for Swap Nodes in Pairs.
# Memory Usage: 13.9 MB, less than 90.54% of Python3 online submissions for Swap Nodes in Pairs.
