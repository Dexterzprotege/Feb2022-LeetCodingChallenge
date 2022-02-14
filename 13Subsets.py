# Question: https://leetcode.com/problems/subsets/

# Solution 1:
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, res, temp, start):
            res.append(temp[:])
            for i in range(start, len(nums)):
                temp.append(nums[i])
                backtrack(nums, res, temp, i+1)
                temp.pop()
        res = []
        nums = sorted(nums)
        backtrack(nums, res, [], 0)
        return res

# Verdict:
# Runtime: 55 ms, faster than 32.02% of Python3 online submissions for Subsets.
# Memory Usage: 14.1 MB, less than 81.42% of Python3 online submissions for Subsets.
