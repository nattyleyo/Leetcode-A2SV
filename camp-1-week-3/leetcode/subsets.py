class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        def backtrack(num,path,length):
            if len(path)==length:
                res.append(path[:])
                return
            for i in range(num,n):
                path.append(nums[i])
                backtrack(i+1,path,length)
                path.pop()
        n = len(nums)
        for i in range(1,n+1):
            backtrack(0,[],i)
        return res