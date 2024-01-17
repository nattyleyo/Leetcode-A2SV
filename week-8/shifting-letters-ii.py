class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n=len(shifts)
        nums=[0]*(len(s)+1)
        ans=['']*len(s)
        for i in range(n):
            left = shifts[i][0]
            right = shifts[i][1]
            k=1 if shifts[i][2]==1 else -1
            nums[left]+=k
            nums[right+1]-=k
        prefix=[0]*len(nums)
        prefix[0]=nums[0]
        for i in range(1,len(nums)):
            prefix[i]=prefix[i-1]+nums[i]
        print(prefix)
        for i in range(len(s)):
            temp=ord('a')-ord(s[i])
            temp%=26
            temp=ord(s[i])-ord('a')+prefix[i]
            temp=temp%26 + ord('a')
            ans[i]=chr(temp)
        return ''.join(ans)


#0  0   0
#-1     1
#   1       -1
#1          -1
#0  1   1   -2

#0  1   2   0

# 0   1   1  -2
        return 'mm'
