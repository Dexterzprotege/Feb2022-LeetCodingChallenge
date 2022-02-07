# Question: https://leetcode.com/problems/find-the-difference/

# ---------------------------------------------------------------------------------------------------- #

# Solution 3: XOR of all elements
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans = 0
        for i in s:
            ans = ans ^ ord(i)
        for i in t:
            ans = ans ^ ord(i)
        return chr(ans)
      
# Verdict:
# Runtime: 36 ms, faster than 76.52% of Python3 online submissions for Find the Difference.
# Memory Usage: 14 MB, less than 88.02% of Python3 online submissions for Find the Difference.

# ---------------------------------------------------------------------------------------------------- #

# Solution 2: Dictionary to keep track
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        for i in t:
            if i not in dic or dic[i] == 0:
                return i
            else:
                dic[i] -= 1

# Vercit:
# Runtime: 54 ms, faster than 33.84% of Python3 online submissions for Find the Difference.
# Memory Usage: 13.9 MB, less than 96.95% of Python3 online submissions for Find the Difference.

# ---------------------------------------------------------------------------------------------------- #

# Solution 1: Sort and check
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(s)
        t = sorted(t)
        for i in range(len(s)):
            if s[i] != t[i]:
                return t[i]
        return t[-1]

# Verdict:
# Runtime: 53 ms, faster than 35.09% of Python3 online submissions for Find the Difference.
# Memory Usage: 13.8 MB, less than 96.95% of Python3 online submissions for Find the Difference.

# ---------------------------------------------------------------------------------------------------- #
