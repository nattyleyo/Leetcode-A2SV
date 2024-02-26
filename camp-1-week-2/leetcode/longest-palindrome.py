class Solution:
    def longestPalindrome(self, s: str) -> int:
        max_len = 0
        count = Counter(s)
        arr = [val for val in count.values()]
        arr.sort(reverse=True)
        n = len(arr)
        if n == 1:
            return arr[0]
        # print(arr)
        odd = False
        for i in range(n):
            if arr[i]%2 != 0 and not odd :
                max_len += arr[i]
                odd = True      
            elif arr[i]%2 != 0 and odd:
                max_len += arr[i]-1
            else:
                max_len += arr[i]
        return max_len
#abccccdd
#{a:1,b:1,c:4,d:2}
#1,1,2,4
#len=4+2