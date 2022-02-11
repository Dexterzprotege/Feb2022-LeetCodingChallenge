# Question: https://leetcode.com/problems/permutation-in-string/

# Solution 1: Brute Force - For all subarrays, sort and compare
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        n = len(s1)
        for i in range(len(s2)-len(s1)+1):
            if sorted(s2[i: i+n]) == s1:
                return True
        return False
      
# Verdict:
# Runtime: 5698 ms, faster than 10.28% of Python3 online submissions for Permutation in String.
# Memory Usage: 14.2 MB, less than 63.89% of Python3 online submissions for Permutation in String.
