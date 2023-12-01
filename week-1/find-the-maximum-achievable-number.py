class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        for i in range(t):
            num+=1
        x=num+t
        return x
        
            