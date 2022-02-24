# Question: https://leetcode.com/problems/sort-list/

# Solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def getMid(head):
            mid = None
            while head and head.next:
                if mid == None:
                    mid = head
                else:
                    mid = mid.next
                head = head.next.next
            m = mid.next
            mid.next = None
            return m
        
        def merge(list1, list2):
            dummy = ListNode()
            tail = dummy
            while list1 !=None and list2!=None:
                if list1.val < list2.val:
                    tail.next = list1
                    list1 = list1.next
                    tail = tail.next
                else:
                    tail.next = list2
                    list2 = list2.next
                    tail = tail.next
            if list1!=None:
                tail.next = list1
            if list2!=None:
                tail.next = list2
            return dummy.next
          
        if head == None or head.next == None:
            return head
        mid = getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return merge(left, right)

# Verdict:
# Runtime: 475 ms, faster than 58.14% of Python3 online submissions for Sort List.
# Memory Usage: 30 MB, less than 91.34% of Python3 online submissions for Sort List.
