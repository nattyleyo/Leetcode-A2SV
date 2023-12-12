class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n=len(queries)
        res=[]
        di={}
        s=set()
        if len(nums)<2:
            return [0]
        evens=sum([num for num in nums if num%2==0])
        for i in range(n):
            val=queries[i][0]
            index=queries[i][1]
            if nums[index]%2==0:
                evens+=-nums[index]
            nums[index]+=val
            if nums[index]%2==0:
                evens+=nums[index]
            res.append(evens)
        return res
        