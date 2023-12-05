class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n=len(num)
        ans=[]
        for i in range(n-2):
            if num[i]==num[i+1] and num[i]==num[i+2]:
                temp=num[i]+num[i+1]+num[i+2]
                ans.append(int(temp))
        if len(ans)==0:
            return ''
        ans.sort()
        largest=ans[len(ans)-1]
        if largest==0:
            return '000'
        return str(largest)
                
                
            
            
            