# Question: https://leetcode.com/problems/summary-ranges/

# Solution:
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        temp = []
        for num in nums:
            if not temp or num != temp[-1][-1] + 1:
                temp.append([num])
            else:
                temp[-1].append(num)
        ans = []
        for i in temp:
            if len(i) == 1:
                ans.append(str(i[0]))
            else:
                ans.append(str(i[0])+"->"+str(i[-1]))
        return ans
      
# Verdict:
# Runtime: 43 ms, faster than 50.47% of Python3 online submissions for Summary Ranges.
# Memory Usage: 13.8 MB, less than 99.05% of Python3 online submissions for Summary Ranges.
