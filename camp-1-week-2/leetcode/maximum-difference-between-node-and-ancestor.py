# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        maxi  = float('-inf')
        mini  = float('inf')
        def preorder(root,maxi,mini):
            if not root:
                return abs(maxi-mini)
            maxi = max(maxi,root.val)
            mini = min(mini,root.val)
            x = preorder(root.left,maxi,mini)
            y = preorder(root.right,maxi,mini)
            return max(x,y)
        return preorder(root,maxi,mini)
#maxi=8
#mini=1
#