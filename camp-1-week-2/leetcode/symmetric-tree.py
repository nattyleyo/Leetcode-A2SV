# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        res =[]
        def inorder(root,flag):
            if root:
                inorder(root.left,'l')
                res.append((root.val, flag))
                inorder(root.right,'r')
        inorder(root,'l')
        # print(res)
        left = 0
        right = len(res)-1
        flag = True
        while left < right:
            if res[left][0] != res[right][0] or res[left][1] == res[right][1] :
                flag = False
            left += 1
            right -= 1

        return flag