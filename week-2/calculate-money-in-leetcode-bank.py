class Solution:
    def totalMoney(self, n: int) -> int:
        amount = 0;
        count=0
        prevMon=val=1
        for i in range(1,n+1):
            amount+=val
            val+=1
            if i%7==0:
                prevMon+=1  
                val=prevMon
        return amount 