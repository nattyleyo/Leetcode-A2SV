class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        minCost = 0
        refund = [0]*n
        for i in range(n):
            refund[i] = costs[i][1] - costs[i][0]
            minCost += costs[i][0]  
        refund.sort()
        for i in range(n//2):
            minCost += refund[i]
        return minCost

#-10 -170 350 10
#10 170 350 10 =540
#-170 -10 10 350
#290
#760-540
220

