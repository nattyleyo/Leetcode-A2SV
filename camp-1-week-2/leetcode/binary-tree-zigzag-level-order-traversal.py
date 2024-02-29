# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        level = 0
        count = defaultdict(list)
        def inorder(root,level):
            if root:
                level  += 1 
                res.append((level,root.val))
                inorder(root.left,level)
                inorder(root.right,level)
        inorder(root,level)
        ans = []
        for i in range(len(res)):
            key = res[i][0]
            tup_val = res[i][1]
            count[key].append(tup_val)
        print(count)
        for key in count:
            elem = count[key]
            if key%2 == 0:
                elem.reverse()
            ans.append(elem)
        # print(ans)

        return ans