class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1,n+1)]
        res = []
        def backtrack(i,path):
            if len(path)==k:
                res.append(path[:])
                return
            if i>= n:
                return
            #insert
            path.append(nums[i])
            backtrack(i+1,path)
            path.pop()
            
            #no insert
            backtrack(i+1,path)

        backtrack(0,[])
        return res
