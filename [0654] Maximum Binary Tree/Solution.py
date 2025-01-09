# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#리컬시브
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        if len(nums) == 1:
            return TreeNode(nums[0])
        tmp_index = 0
        tmp = nums[tmp_index]
        for i in range(len(nums)):
            if nums[i] > tmp:
                tmp = nums[i]
                tmp_index = i
        tmp_left = nums[:tmp_index]
        tmp_right = nums[tmp_index+1 : ]
        root = TreeNode(tmp)
        if tmp_left != []:
            root.left = self.constructMaximumBinaryTree(tmp_left)
        if tmp_right != []:
            root.right = self.constructMaximumBinaryTree(tmp_right)
        return root
        