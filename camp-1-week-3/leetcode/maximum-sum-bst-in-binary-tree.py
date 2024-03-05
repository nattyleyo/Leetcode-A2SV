# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.maxiSum = 0
        
        def postorder(root):
            if not root:
                return True, float('inf'), float('-inf'), 0

            leftValid, leftMin, leftMax, leftSum = postorder(root.left)
            rightValid, rightMin, rightMax, rightSum = postorder(root.right)
            # print(leftSum)
            if leftValid and rightValid and leftMax < root.val < rightMin:
                currSum = leftSum + rightSum + root.val
                self.maxiSum = max(self.maxiSum, currSum)
                return True, min(leftMin, root.val), max(rightMax, root.val), currSum
            else:
                return False, None, None, None

        postorder(root)
        return self.maxiSum
