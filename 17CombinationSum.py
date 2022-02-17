# Question: https://leetcode.com/problems/combination-sum/

# Solution:
class Solution:
    def backtrack(self, curr, target, index):
        if target == 0:
            self.combinations.append(curr)
            return 
        if target < 0:
            return 
        for i in range(index, len(self.candidates)):
            tmp = curr + [self.candidates[i]]
            self.backtrack(tmp, target-self.candidates[i], i)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.combinations = []
        self.candidates = sorted(candidates)
        self.backtrack([], target, 0)
        return self.combinations

# Verdict:
# Runtime: 123 ms, faster than 41.24% of Python3 online submissions for Combination Sum.
# Memory Usage: 14 MB, less than 87.78% of Python3 online submissions for Combination Sum.
