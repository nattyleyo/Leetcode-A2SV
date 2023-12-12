class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        di={}
        n=len(nums)
        di[nums[0]]=1
        res=[]
        for i in range(1,n):
            if nums[i] in di:
                di[nums[i]]+=1
            else:
                di[nums[i]]=1
        for num in di:
            if di[num] > n/3:
                res.append(num)
        return res        