class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        for i in range(n-1, -1, -1):
            temp = int(num[i])
            if temp % 2 != 0:
                num=num[:i+1]
                return num
        return ''
        
        


        