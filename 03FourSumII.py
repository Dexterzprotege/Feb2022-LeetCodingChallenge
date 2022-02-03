# Question: https://leetcode.com/problems/4sum-ii/

# -------------------------------------------------------------------------------------------------------------- #

# Solution 3: Removing two loops O(N^2)
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = 0
        hm = defaultdict(int)
        for k in nums3:
            for l in nums4:
                hm[k+l] += 1
        for i in nums1:
            for j in nums2:
                if hm[-(i+j)]:
                    count += hm[-(i+j)]
        return count
    
# Verdict:
# Runtime: 1167 ms, faster than 30.85% of Python3 online submissions for 4Sum II.
# Memory Usage: 14.1 MB, less than 99.75% of Python3 online submissions for 4Sum II.

# -------------------------------------------------------------------------------------------------------------- #

# Solution 2: Removing one loop O(N^3)
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = 0
        hm = defaultdict(int)
        for l in nums4:
            hm[l] += 1
        for i in nums1:
            for j in nums2:
                for k in nums3:
                    if hm[-(i+j+k)]:
                        count += hm[-(i+j+k)]
        return count
    
# Verdict:
TLE

# -------------------------------------------------------------------------------------------------------------- #

# Solution 1: Brute Force O(N^4)
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = 0
        for i in nums1:
            for j in nums2:
                for k in nums3:
                    for l in nums4:
                        if i+j+k+l == 0:
                            count += 1
        return count

# Verdict:
TLE

# -------------------------------------------------------------------------------------------------------------- #
