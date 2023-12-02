class Solution:
    def average(self, salary: List[int]) -> float:
        salary=sorted(salary)
        n=len(salary)
        sum=0
        for i in range(1,n-1):
            sum+=salary[i]
        average=sum/(n-2)
        return average