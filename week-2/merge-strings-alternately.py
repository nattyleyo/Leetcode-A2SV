class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n=len(word1)
        m=len(word2)
        merge=""
        for i in range(max(n,m)):
            if i<n:
                merge+=word1[i]
            if i<m:
                merge+=word2[i]
        return merge   
               
             
            
            