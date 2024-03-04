class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()
        def backtrack(idx,path,length):
            if len(path)==length and path[:] not in res:
                res.append(path[:])
                return
            
            for i in range(idx,n):
                path.append(nums[i])
                backtrack(i+1,path,length)
                path.pop()
        n = len(nums)
        for i in range(1,n+1):
            backtrack(0,[],i)
        return res