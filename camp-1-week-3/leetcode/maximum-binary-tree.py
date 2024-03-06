# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        left = 0
        right = len(nums)-1
        
        def helper(nums,left,right):
            if left > right:
                return None
            maxi = max(nums[left:right+1])
            maxi_idx = nums.index( maxi )

            root = TreeNode(maxi)
            root.left = helper(nums,left,maxi_idx -1)
            root.right = helper(nums,maxi_idx + 1,right)
            return root
        return helper(nums, left,right)


                
