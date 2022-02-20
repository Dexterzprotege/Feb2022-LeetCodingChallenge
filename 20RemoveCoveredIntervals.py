# Question: https://leetcode.com/problems/remove-covered-intervals/

# Solution:
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        intervals = sorted(intervals)
        currInterval = [-1, -1]
        for interval in intervals:
            if interval[0] > currInterval[0] and interval[1] > currInterval[1]:
                currInterval[0] = interval[0]
                ans += 1
            currInterval[1] = max(currInterval[1], interval[1])
        return ans
            
# Verdict:
# Runtime: 151 ms, faster than 40.52% of Python3 online submissions for Remove Covered Intervals.
# Memory Usage: 14.4 MB, less than 96.36% of Python3 online submissions for Remove Covered Intervals.
