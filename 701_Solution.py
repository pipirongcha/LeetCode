# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        tmp = root


        while tmp.left or tmp.right:
            if tmp.right and not tmp.left:
                if tmp.val < val:
                    tmp = tmp.right
                else: 
                    tmp.left = TreeNode(val)
                    break
            if tmp.left and not tmp.right:
                if tmp.val > val:
                    tmp = tmp.left
                else: 
                    tmp.right = TreeNode(val)
                    break
            if tmp.left and tmp.right:
                if tmp.val > val:
                    tmp = tmp.left
                else:
                    tmp = tmp.right

        if tmp.val > val:
            tmp.left = TreeNode(val)
        else:
            tmp.right = TreeNode(val)

        return root