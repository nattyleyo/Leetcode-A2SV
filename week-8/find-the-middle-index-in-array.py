class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n=len(nums)
        left=0
        right=0
        pref=0
        total=sum(nums)
        for i in range(n):
            pref+=nums[i]
            left = pref - nums[i]
            right = total - pref
            if left==right:
                return i
        # print(pref)
        return -1
        


#2 3 -1 8 4
#       ^

#pref=12
# L=4
# R=4