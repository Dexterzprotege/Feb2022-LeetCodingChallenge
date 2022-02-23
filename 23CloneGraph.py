# Question: https://leetcode.com/problems/clone-graph/

# Solution:
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        dic = {}
        
        def dfs(node):
            if node in dic:
                return dic[node]
            
            copy = Node(node.val)
            dic[node] = copy
            
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy
        
        return dfs(node) if node else None
      
# Verdict:
# Runtime: 34 ms, faster than 94.04% of Python3 online submissions for Clone Graph.
# Memory Usage: 14.4 MB, less than 66.44% of Python3 online submissions for Clone Graph.
