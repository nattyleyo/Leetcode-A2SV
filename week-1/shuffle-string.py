class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        p=0
        strLen=len(s)
        indLen=len(indices)
        res=[0]*strLen
        for index in range(strLen):
            newIndex=indices[index]
            res[newIndex]=s[index]
        return ''.join(res)
            
                