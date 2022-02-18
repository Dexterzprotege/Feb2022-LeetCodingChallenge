# Question: https://leetcode.com/problems/remove-k-digits/

# Solution:
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for n in num:
            while stack and stack[-1] > n and k:
                stack.pop()
                k -= 1
            if stack or n is not '0':
                stack.append(n)
        if k:
            while k and stack:
                stack.pop()
                k -= 1
        ans = ''.join(stack)
        return ans if ans else '0'
      
# Verdict:
# Runtime: 69 ms, faster than 36.75% of Python3 online submissions for Remove K Digits.
# Memory Usage: 14.1 MB, less than 93.92% of Python3 online submissions for Remove K Digits.
