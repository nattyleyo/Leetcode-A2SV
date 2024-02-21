class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        flag = True
        di = defaultdict(int)
        for i in range(len(bills)):
            if bills[i] == 5:
                di[5] += 1
            elif bills[i] == 10 and di[5] > 0:
                di[5] -= 1
                di[10] += 1
            elif bills[i] == 20 and di[10] > 0 and di[5] > 0:
                di[5] -= 1
                di[10] -= 1
            elif bills[i] == 20 and di[10] < 1 and di[5] >= 3:
                di[5] -= 3
            else:
                return False
        return True
             
            
#5  5  5 10  20    
#         ^
#net=2
#val=1
#{5:2,10:1,20:1}