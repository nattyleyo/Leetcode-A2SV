class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def backtrack(idx,path):
            if sum(path)== n and len(path) == k:
                res.append(path[:])
                return
            # if sum(path) > n:
            #     return
            for i in range(idx,10):
                path.append(i)
                backtrack(i+1,path)
                path.pop()
        backtrack(1,[])
        return res
