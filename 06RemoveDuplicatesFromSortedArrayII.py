# Question: /remove-duplicates-from-sorted-array-ii/

# Solution:
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for n in nums:
            if i < 2 or n > nums[i-2]:
                nums[i] = n
                i += 1
        return i
      
# Verdict:
# Runtime: 75 ms, faster than 45.46% of Python3 online submissions for Remove Duplicates from Sorted Array II.
# Memory Usage: 13.9 MB, less than 89.34% of Python3 online submissions for Remove Duplicates from Sorted Array II.
