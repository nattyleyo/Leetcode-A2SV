class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        left=0
        right=1
        dup=0
        k=1
        count=0
        while right<n:
            if left ==right:
                right+=1
            elif nums[left]==nums[right]:
                nums[right]='_'
                count+=1
                right+=1
            elif nums[left]=='_':
                nums[left],nums[right]=nums[right],nums[left]
                right+=1
            elif nums[right]=='_':
                right+=1
            else:
                left+=1
            k= n- count
        return k
#0  1   1   1   2   2   3   3   4
#^  ^ 