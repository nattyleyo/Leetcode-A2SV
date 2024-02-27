class Solution:
    def decodeString(self, s: str) -> str:
        res = []
        def helper(s,start)->str:
            tempStr = ''
            num = 0
            while start < len(s):
                if s[start] == ']':
                    return tempStr , start
                elif s[start].isdigit():
                    num =num * 10 + int(s[start])

                elif s[start] == '[':
                    resFunc , start = helper(s,start+1)
                    tempStr += num*resFunc
                    num = 0
                else:
                    tempStr += s[start]
                start += 1
            return tempStr , start
        return helper(s,0)[0]
