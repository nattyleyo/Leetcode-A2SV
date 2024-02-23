class Solution:
    def balancedString(self, s: str) -> int:
        count = defaultdict(int)
        length = len(s)
        need = length / 4
        window = length
        left = 0
        for i in range(length):
            count[s[i]] += 1
        for right in range(length):
            count[s[right]] -= 1
            while max(count.values()) <= need:
                if left >= length:
                    break
                count[s[left]] += 1
                window = min(window,right-left+1)
                left += 1
        return window


#tar=1
#012345678901
#  *
#wwQQRRRRQRQQ
#          ^
#{w:2,Q:4,R:2,E:0}
#win=6
        
        