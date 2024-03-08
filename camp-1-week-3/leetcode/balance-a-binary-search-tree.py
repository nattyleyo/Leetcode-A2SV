# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        res = []
        # print(root.val)
        def inorder(root):
            if root:
                inorder(root.left)
                res.append(root.val)
                inorder(root.right)
        inorder(root)
        # print(res)
        left = 0
        right = len(res)-1
        def helper(left,right):
            if left > right:
                return None
            mid = (left + right)//2
            result = TreeNode(res[mid])
            result.left = helper(left,mid-1)
            result.right = helper(mid+1,right)
            return result
        ans = helper(left,right)
        # print(ans)
        return ans