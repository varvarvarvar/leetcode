"""
You need to find the largest value in each row of a binary tree.

Example:
Input:

          1
         / \
        3   2
       / \   \
      5   3   9

Output: [1, 3, 9]
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        if not root:
            return []
        maxes = []
        current_row = [root]
        while current_row:
            maxes.append(max((el.val for el in current_row)))
            current_row = [child for el in current_row for child in (el.left, el.right) if child]
        return maxes
