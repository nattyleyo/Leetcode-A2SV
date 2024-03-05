# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        count = defaultdict(list)
        def preorder(root,level,idx):
            if not root:
                return
            if root:
                # level += 1    
                count[level].append(idx)
                
                preorder(root.left,level+1,2*idx)
                preorder(root.right,level+1,2*idx + 1)
        preorder(root,1,1)
        maxi = float('-inf')
        for key in count:
            width = max(count[key])-min(count[key]) + 1
            maxi = max( maxi , width )
        # print(count)
        return maxi