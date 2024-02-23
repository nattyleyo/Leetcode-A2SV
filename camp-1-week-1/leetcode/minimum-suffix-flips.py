class Solution:
    def minFlips(self, target: str) -> int:
        ones = False
        res = 0
        for i in range(len(target)):
            if not ones and target[i] == '1':
                ones = True
                res += 1
            if ones and target[i] == '0':
                ones = False
                res += 1
        return res
#01234
#110001
#  ^
#ones=f
#ans=2
# #10111}