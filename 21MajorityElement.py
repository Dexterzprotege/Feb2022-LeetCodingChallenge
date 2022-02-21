# Question: https://leetcode.com/problems/majority-element/

# --------------------------------------------------------------------------------------------- #

# Solution 5: Boyer Moore Majority vote algorithm O(N) + O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if count == 0:
                count += 1
                major = nums[i]
            elif major == nums[i]:
                count += 1
            else:
                count -= 1
        return major
      
# Verdict:
# Runtime: 289 ms, faster than 22.88% of Python3 online submissions for Majority Element.
# Memory Usage: 15.7 MB, less than 8.22% of Python3 online submissions for Majority Element.

# --------------------------------------------------------------------------------------------- #

# Solution 4: Greedy - Divide and conquer O(NLogN) + O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def count(nums, left, right, val):
            count = 0
            for i in range(left, right):
                if nums[i] == val:
                    count += 1
            return count
        def majority(nums, left, right):
            if left == right:
                return nums[left]
            mid = left + (right - left)//2
            lm = majority(nums, left, mid)
            rm = majority(nums, mid+1, right)
            if lm == rm:
                return lm
            
            leftCount = count(nums, left, right+1, lm)
            rightCount = count(nums, left, right+1, rm)
            
            return lm if leftCount > rightCount else rm
        return majority(nums, 0, len(nums)-1)
      
# Verdict:
# Runtime: 252 ms, faster than 39.46% of Python3 online submissions for Majority Element.
# Memory Usage: 15.5 MB, less than 43.74% of Python3 online submissions for Majority Element.

# --------------------------------------------------------------------------------------------- #
  
# Solution 3: Randomization O(∞) + O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        import random
        
        n = len(nums)
        while True:
            candidate = nums[random.randint(0, n-1)]
            count = 0
            for num in nums:
                if num == candidate:
                    count += 1
            if count > n//2:
                break
        return candidate
      
# Verdict:
# Runtime: 276 ms, faster than 28.75% of Python3 online submissions for Majority Element.
# Memory Usage: 15.4 MB, less than 81.81% of Python3 online submissions for Majority Element.

# --------------------------------------------------------------------------------------------- #

# Solution 2: Sorting O(NLogN) + O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]
      
# Verdict:
# Runtime: 168 ms, faster than 86.56% of Python3 online submissions for Majority Element.
# Memory Usage: 15.5 MB, less than 43.74% of Python3 online submissions for Majority Element.

# --------------------------------------------------------------------------------------------- #

# Solution 1: Hashing O(N) + O(N)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        for i in nums:
            dic[i] += 1
        for key, val in dic.items():
            if val > len(nums)//2 :
                return key
              
# Verdict:
# Runtime: 248 ms, faster than 41.21% of Python3 online submissions for Majority Element.
# Memory Usage: 15.4 MB, less than 81.81% of Python3 online submissions for Majority Element.

# --------------------------------------------------------------------------------------------- #
