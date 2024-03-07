class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        ans = list(palindrome)
        count = 1
        left = 0
        right = 0
        if len(palindrome)==1:
            return ''
        temp = ''
        for i in range(len(palindrome)):
            if palindrome[i] != 'a':
                temp = ans[i]
                ans[i] = 'a'
                if all( char=='a' for char in ans):
                    ans[i] = temp
                    ans[-1] = 'b'
                return ''.join(ans)

        ans[-1] = 'b'
        return ''.join(ans)



