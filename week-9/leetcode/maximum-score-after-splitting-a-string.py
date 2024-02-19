class Solution:
    def maxScore(self, s: str) -> int:
        maxS = 0
        ones = s.count('1')
        zeros = 0
        n = len(s)
        for i in range(n-1):
            if s[i] == '1':
                ones -=1
            else:
                zeros +=1
            maxS = max( maxS, ones + zeros)
        return maxS
                

#011101
#  ^
#1==2
#0==1
#r==4  