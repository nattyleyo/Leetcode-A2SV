# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        level = 0
        count = defaultdict(list)
        res = []
        digit = 0
        def inorder(root,digit):
            if not root:
                return 0
            digit = digit*10 + root.val
            if not root.left and not root.right:
                return digit
            else: 
                x = inorder(root.left, digit)
                y = inorder(root.right, digit)
                return x+y
        return inorder(root,digit)
        