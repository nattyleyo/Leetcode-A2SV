class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        di=defaultdict(lambda:1)
        n=len(nums)
        res=[]
        for i in range(0,n):
            if nums[i] in di:
                di[nums[i]]+=1
            else:
                di[nums[i]]=1
        for num in di:
            if di[num] > n/2:
                res.append(num)
        return res[0]   

                


        