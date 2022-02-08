# Question: https://leetcode.com/problems/add-digits/

# ----------------------------------------------------------------------------------- #

# Solution 2: Math O(1)
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9

# Verdict:
# Runtime: 32 ms, faster than 83.79% of Python3 online submissions for Add Digits.
# Memory Usage: 14 MB, less than 81.53% of Python3 online submissions for Add Digits.

# ----------------------------------------------------------------------------------- #

# Solution 1: brute force: Iterative
class Solution:
    def addDigits(self, num: int) -> int:
        ans = 0
        while num > 0:
            ans += num % 10
            num = num//10
            if num == 0 and ans > 9:
                num = ans
                ans = 0
        return ans

# Verdict:
# Runtime: 53 ms, faster than 28.21% of Python3 online submissions for Add Digits.
# Memory Usage: 13.7 MB, less than 99.39% of Python3 online submissions for Add Digits.

# ----------------------------------------------------------------------------------- #
