# Question: https://leetcode.com/problems/compare-version-numbers/

# Solution:
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        for i in range(len(v1)):
            v1[i] = int(v1[i])
        for i in range(len(v2)):
            v2[i] = int(v2[i])
        
        i = 0
        while i < len(v1) or i < len(v2):
            a = v1[i] if i < len(v1) else 0
            b = v2[i] if i < len(v2) else 0
            if a < b:
                return -1
            elif a > b:
                return 1
            i += 1
        return 0
            
            
# Verdict:
# Runtime: 49 ms, faster than 34.42% of Python3 online submissions for Compare Version Numbers.
# Memory Usage: 13.9 MB, less than 92.33% of Python3 online submissions for Compare Version Numbers.
