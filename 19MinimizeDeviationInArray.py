# Question: https://leetcode.com/problems/minimize-deviation-in-array/

# Solution:
class Solution:
    def minimumDeviation(self, A):
        pq = []
        for a in A:
            heapq.heappush(pq, [a / (a & -a), a])
        res = float('inf')
        ma = max(a for a, a0 in pq)
        while len(pq) == len(A):
            a, a0 = heapq.heappop(pq)
            res = min(res, ma - a)
            if a % 2 == 1 or a < a0:
                ma = max(ma, a * 2)
                heapq.heappush(pq, [a * 2, a0])
        return int(res)

# Verdict:
# Runtime: 1048 ms, faster than 73.79% of Python3 online submissions for Minimize Deviation in Array.
# Memory Usage: 31.8 MB, less than 25.24% of Python3 online submissions for Minimize Deviation in Array.
