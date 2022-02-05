# Question: https://leetcode.com/problems/merge-k-sorted-lists/

# Solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    from heapq import heappush, heappop
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode(0)
        curr = head
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next
        while heap:
            val, i = heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next
            if lists[i]:
                heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next
        return head.next

# Verdict:
# Runtime: 117 ms, faster than 68.69% of Python3 online submissions for Merge k Sorted Lists.
# Memory Usage: 17.6 MB, less than 97.61% of Python3 online submissions for Merge k Sorted Lists.
