# Question: https://leetcode.com/problems/k-diff-pairs-in-an-array/

# ----------------------------------------------------------------------------------------------- #

# Solution 4: HashSet count the occurrences and determine: O(N) + O(N)
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        for i in nums:
            dic[i] += 1
        ans = 0
        for key in dic.keys():
            if (k > 0 and key+k in dic) or (k == 0 and dic[key] > 1):
                ans += 1
        return ans

# Verdict:
# Runtime: 97 ms, faster than 57.21% of Python3 online submissions for K-diff Pairs in an Array.
# Memory Usage: 15.7 MB, less than 52.69% of Python3 online submissions for K-diff Pairs in an Array.

# ----------------------------------------------------------------------------------------------- #

# Solution 3: Sort and two pointers: O(NLogN) + O(1)
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k == 0:
            freqs = Counter(nums)
            return sum(freqs[k] > 1 for k in freqs)
        nums = sorted(set(nums))
        left, right = 0, 0
        ans = 0
        while right < len(nums):
            diff = nums[right] - nums[left]
            if diff < k:
                right += 1
            elif diff > k:
                left += 1
            else:
                ans += 1
                left += 1
                right += 1
        return ans

# Verdict:
# Runtime: 94 ms, faster than 58.96% of Python3 online submissions for K-diff Pairs in an Array.
# Memory Usage: 15.9 MB, less than 35.43% of Python3 online submissions for K-diff Pairs in an Array.

# ----------------------------------------------------------------------------------------------- #

# Solution 2: Sort and search for arr[i]+k in the array O(NLogN) + O(N) 
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        s = set()
        for i in range(len(nums)-1):
            if nums[i]+k in nums[i+1:]:
                s.add(nums[i])
        return len(s)
      
# Verdict:
# Runtime: 876 ms, faster than 5.24% of Python3 online submissions for K-diff Pairs in an Array.
# Memory Usage: 15.8 MB, less than 40.07% of Python3 online submissions for K-diff Pairs in an Array.

# ----------------------------------------------------------------------------------------------- #

# Solution 1: Brute Force: O(N2) + O(N)
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ans = 0
        s = set()
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i]-nums[j] == k:
                    s.add(nums[i])
        return len(s)

# Verdict:
TLE

# ----------------------------------------------------------------------------------------------- #
