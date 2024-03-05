class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter = {2:'abc',3:'def',4:'ghi',5:'jkl',
        6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
        res = []
        if len(digits)==0:
            return res
        def backtrack(idx,path):
            if len(path) == len(digits):
                res.append(''.join( path[:]))
                return
            for i in range(idx,len(digits)):
                dig = int(digits[i])
                length = len(letter[ dig ])

                for j in range(length):
                    val = letter[dig][j]
                    # if len(path)>0 and path[-1] in letter[dig] and val in letter[dig]:
                    #     continue
                    path.append(val)
                    backtrack(i+1,path)
                    path.pop()
        
        backtrack(0,[])
        # print(res)
        return res