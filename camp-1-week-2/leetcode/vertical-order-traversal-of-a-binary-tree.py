# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        row = 0 
        col = 0
        count = defaultdict(list)
        ans = []
        def inorder(root,row,col):
            if root:
                inorder(root.left,row+1,col-1)
                count[col].append((row,root.val))
                inorder(root.right,row+1,col+1)
        inorder(root,row,col)
        count = dict(sorted(count.items()))
        for key in count:
            elem = count[key]
            elem.sort()
            temp = []
            for i in range(len(elem)):
                temp.append( elem[i][1] )              
            ans.append( temp )
        # print(ans)
        
        return ans