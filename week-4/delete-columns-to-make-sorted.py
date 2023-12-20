class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        row=len(strs)
        col=len(strs[0])
        count=0
        for j in range(col):
            for i in range(row-1):
                if strs[i][j]>strs[i+1][j]:
                    count+=1
                    break
        return count