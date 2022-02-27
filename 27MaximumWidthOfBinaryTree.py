# Question: https://leetcode.com/problems/maximum-width-of-binary-tree/

# Solution:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        width = 0
        level = [(1, root)]
        while level:
            width = max(width, level[-1][0] - level[0][0] + 1)
            level = [kid
                     for number, node in level
                     for kid in enumerate((node.left, node.right), 2 * number)
                     if kid[1]]
        return width
      
# Verdict:
# Runtime: 86 ms, faster than 16.49% of Python3 online submissions for Maximum Width of Binary Tree.
# Memory Usage: 14.8 MB, less than 69.75% of Python3 online submissions for Maximum Width of Binary Tree.
