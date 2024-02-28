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
                # res.append(root.val)
                count[root.val] += 1
                preorder(root.left)
                preorder(root.right)
            
        preorder(root)
        # print(count)
        maxi = max(count.values())
        # print(maxi)
        for key in count:
            if count[key] == maxi:
                res.append(key)
                # break
        return res