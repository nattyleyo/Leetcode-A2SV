# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count = defaultdict(int)
        res =[]
        def preorder(root):
            if root:
                count[root.val] += 1
                preorder(root.left)
                preorder(root.right)
            
        preorder(root)
        maxi = max(count.values())
        for key in count:
            if count[key] == maxi:
                res.append(key)
        return res