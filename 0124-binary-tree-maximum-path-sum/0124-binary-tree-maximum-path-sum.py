# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node:
                return 0
            left=max(helper(node.left),0)
            right=max(helper(node.right),0)
            maxnode=node.val+left+right
            self.maxSum=max(self.maxSum,maxnode)
            return node.val+max(left,right)
        self.maxSum = float('-inf')
        helper(root)
        return self.maxSum