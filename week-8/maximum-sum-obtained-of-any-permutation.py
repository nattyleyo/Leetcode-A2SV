class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        ar=[0]*(len(nums)+1)
        for request in requests:
            ar[request[0]]+=1
            ar[request[1]+1]-=1
        _sum=0
        for i in range(len(ar)):
            _sum+=ar[i]
            ar[i]=_sum
        ar.pop()
        ar.sort(reverse=True)
        nums.sort(reverse=True)
        i=0
        total=0
        while(i<len(nums ) and ar[i]!=0 ):
            total+=nums[i]*ar[i]
            i+=1
        return total%(10**9 + 7)