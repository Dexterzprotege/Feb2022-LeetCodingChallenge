# Question: https://leetcode.com/problems/find-all-anagrams-in-a-string/

# Solution 1: Brute Force
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def checkAnagram(a, b):
            return sorted(a) == sorted(b)
        ans = []
        n, m = len(s), len(p)
        for i in range(0, n-m+1):
            if checkAnagram(s[i:i+m], p):
                ans.append(i)
        return ans

# Verdict:
TLE
