# Question: https://leetcode.com/problems/find-all-anagrams-in-a-string/

# ------------------------------------------------------------------------------------------------------------------ #

# Solution 2: Sliding Window Technique
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def frequency(s):
            count = [0]*26
            for i in range(len(s)):
                count[ord(s[i]) - ord('a')] += 1
            return count
        ans = []
        if len(p) > len(s):
            return ans
        n = len(s)
        m = len(p)
        count = frequency(p)
        currentCount = frequency(s[0: m])
        if count == currentCount:
            ans.append(0)
        for i in range(m, n):
            currentCount[ord(s[i-m]) - ord('a')] -= 1
            currentCount[ord(s[i]) - ord('a')] += 1
            if count == currentCount:
                ans.append(i-m+1)
        return ans
    
# Verdict:
# Runtime: 126 ms, faster than 77.38% of Python3 online submissions for Find All Anagrams in a String.
# Memory Usage: 15.3 MB, less than 10.05% of Python3 online submissions for Find All Anagrams in a String.

# ------------------------------------------------------------------------------------------------------------------ #    

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

# ------------------------------------------------------------------------------------------------------------------ #
