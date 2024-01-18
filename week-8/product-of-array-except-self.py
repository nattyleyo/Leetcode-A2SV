class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pref=[0]*n
        suff=[0]*n

        pref[0]=nums[0]
        suff[n-1]=nums[n-1]
        prod=1
        res=[0]*n
        for i in range(1,n):
            pref[i]=pref[i-1]*nums[i]
        prod=1
        for i in range(n-1,-1,-1):
            suff[i]=prod
            prod*=nums[i]
        print(pref)
        print(suff)
        res[0]=suff[0]
        for i in range(1,n):
            res[i]=pref[i-1]* suff[i]
        # res=[abs(num) for num in res]
        # print(res)
        return res
        


