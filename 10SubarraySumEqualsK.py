# Question: https://leetcode.com/problems/subarray-sum-equals-k/

# Solution:
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, ans = 0, 0
        dic = defaultdict(int)
        dic[0] = 1
        for i in range(len(nums)):
            ans += nums[i]
            if ans-k in dic:
                count += dic[ans-k]
            dic[ans] = dic[ans] + 1
        return count

# Verdict:
# Runtime: 497 ms, faster than 10.00% of Python3 online submissions for Subarray Sum Equals K.
# Memory Usage: 16.6 MB, less than 93.61% of Python3 online submissions for Subarray Sum Equals K.
