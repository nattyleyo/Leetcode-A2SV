class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(idx,path,length):
            if sum(path) == target and path[:] not in res:
                res.append(path[:])
                return
            if sum(path) > target:
                return 
            for i in range(idx,n):
                # print()
                if i > idx and candidates[i-1] == candidates[i]:
                    continue
                path.append(candidates[i])
                backtrack(i+1,path,length)
                path.pop()
        n = len(candidates)
        for i in range(1,n+1):
            backtrack(0,[],i)

        return res