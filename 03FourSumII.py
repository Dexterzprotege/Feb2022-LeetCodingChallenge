# Question: https://leetcode.com/problems/4sum-ii/

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
