# Question: https://leetcode.com/problems/permutation-in-string/

# ------------------------------------------------------------------------------------------------------ #

# Solution 4: Rolling hash, similar to below but better O(N)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):   
            return False
        a = defaultdict(int)
        b = defaultdict(int)
        for i in range(len(s1)):
            a[ord(s1[i])-ord('a')] += 1
            b[ord(s2[i])-ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if a[i] == b[i]:
                matches += 1
        
        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            # Add next value
            index = ord(s2[right]) - ord('a')
            b[index] += 1
            if a[index] == b[index]:
                matches += 1
            elif a[index] + 1 == b[index]:
                matches -= 1
                
            # Remove first value
            index = ord(s2[left]) - ord('a')
            b[index] -= 1
            if a[index] == b[index]:
                matches += 1
            elif a[index] - 1 == b[index]:
                matches -= 1
            
            left += 1
        return matches == 26
            
# Verdict: 
# Runtime: 88 ms, faster than 70.72% of Python3 online submissions for Permutation in String.
# Memory Usage: 13.9 MB, less than 93.32% of Python3 online submissions for Permutation in String.

# ------------------------------------------------------------------------------------------------------ #

# Solution 3: Rolling hash, sliding window O(26*N)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a = defaultdict(int)
        b = defaultdict(int)
        for i in s1:
            a[i] += 1
        initial_window = s2[:len(s1)]
        for i in initial_window:
            b[i] += 1
        if a == b:
            return True
        for i in range(len(s2)-len(s1)):
            # Remove first value
            if b[s2[i]] == 1:
                del b[s2[i]]
            elif b[s2[i]] > 1:
                b[s2[i]] -= 1
            # Add next value
            if s2[i+len(s1)] in b:
                b[s2[i+len(s1)]] += 1
            else:
                b[s2[i+len(s1)]] = 1
            if a == b:
                return True
        return False
    
# Verdict:
# Runtime: 106 ms, faster than 59.56% of Python3 online submissions for Permutation in String.
# Memory Usage: 14.1 MB, less than 83.82% of Python3 online submissions for Permutation in String.

# ------------------------------------------------------------------------------------------------------ #

# Solution 2: Hashing, compare two windows: O(NK)+ O(1)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a = defaultdict(int)
        for i in s1:
            a[i] += 1
        for i in range(len(s2)):         # ---- O(n)
            substr = s2[i: i+len(s1)]    # ---- O(k)
            b = defaultdict(int)
            for j in substr:             # ---- O(k)
                b[j] += 1
            if a == b:
                return True
        return False

# Verdict:
# Runtime: 7715 ms, faster than 5.01% of Python3 online submissions for Permutation in String.
# Memory Usage: 13.8 MB, less than 99.16% of Python3 online submissions for Permutation in String.
    
# ------------------------------------------------------------------------------------------------------ #

# Solution 1: Brute Force - For all subarrays, sort and compare: O(N2LogN)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)   # ---- O(NLogN)
        n = len(s1)
        for i in range(len(s2)-len(s1)+1):  # ---- O(n)
            if sorted(s2[i: i+n]) == s1:    # ---- O(nlogn)
                return True
        return False
      
# Verdict:
# Runtime: 5698 ms, faster than 10.28% of Python3 online submissions for Permutation in String.
# Memory Usage: 14.2 MB, less than 63.89% of Python3 online submissions for Permutation in String.

# ------------------------------------------------------------------------------------------------------ #
