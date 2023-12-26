class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n=len(names)
        minIdx=0
        for i in range(n):
            for j in range(i,n):
                if heights[i]<heights[j]:
                    names[i],names[j]=names[j],names[i]   
                    heights[i],heights[j]=heights[j],heights[i] 
                    minIdx+=1
        return names

        