# Question: https://leetcode.com/problems/excel-sheet-column-number/

# Solution:
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        poww = 0
        for i in columnTitle[::-1]:
            ans += (ord(i)-ord('A')+1) * (26**poww)
            poww += 1
        return ans
      
# Verdict:
# Runtime: 32 ms, faster than 90.14% of Python3 online submissions for Excel Sheet Column Number.
# Memory Usage: 14 MB, less than 62.82% of Python3 online submissions for Excel Sheet Column Number.
