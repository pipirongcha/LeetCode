# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        return self.dfs(p) == self.dfs(q)

    def dfs(self, node):
        if not node:
            return []

        else:
            left = self.dfs(node.left)
            right = self.dfs(node.right)

            return [left + [node.val] + right]