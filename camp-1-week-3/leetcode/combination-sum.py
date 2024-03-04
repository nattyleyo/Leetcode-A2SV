class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(path):
            if sum(path)== target:
                path = path[:]
                path.sort()
                if path not in res:
                    res.append(path)
                return 
            for i in range(len(candidates)):
                if sum(path) > target:
                    continue
                path.append(candidates[i])
                backtrack(path)
                path.pop()
        backtrack([])
        # print(res)
        return res
    