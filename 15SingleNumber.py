# Question: https://leetcode.com/problems/single-number/submissions/

# ----------------------------------------------------------------------------------------- #

# Solution: Bitmanipulation XOR O(N) + O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = nums[0]
        for i in nums[1:]:
            ans = ans ^ i
        return ans

# Verdict:
# Runtime: 152 ms, faster than 65.82% of Python3 online submissions for Single Number.
# Memory Usage: 16.8 MB, less than 30.94% of Python3 online submissions for Single Number.

# ----------------------------------------------------------------------------------------- #

# Solution: Hashmap O(N) + O(N)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        for i in nums:
            dic[i] += 1
        for key, val in dic.items():
            if val == 1:
                return key
              
# Verdict:
# Runtime: 240 ms, faster than 28.60% of Python3 online submissions for Single Number.
# Memory Usage: 16.7 MB, less than 30.94% of Python3 online submissions for Single Number.

# ----------------------------------------------------------------------------------------- #

# Solution: Math O(N) + O(N)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2*sum(set(nums))-sum(nums)
      
# Verdict:
# Runtime: 150 ms, faster than 66.43% of Python3 online submissions for Single Number.
# Memory Usage: 17.1 MB, less than 6.05% of Python3 online submissions for Single Number.

# ----------------------------------------------------------------------------------------- #
