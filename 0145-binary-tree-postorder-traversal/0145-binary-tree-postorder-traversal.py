# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        self.postorder(root,l)
        return l
    def postorder(self,root,l):
        if root is None:
            return
        self.postorder(root.left,l)
        self.postorder(root.right,l)
        l.append(root.val)