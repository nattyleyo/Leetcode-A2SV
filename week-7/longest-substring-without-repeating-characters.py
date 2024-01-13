class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=0
        window={}
        longSub=0
        while right<len(s):
            if s[right] in window and window[s[right]] >= left:
                left=window[s[right]]+1
            window[s[right]]=right
            longSub=max(longSub,right-left+1)
            right+=1
        return longSub
#01234567
#abcabcbb
#       ^
#       ^

#{b:6,c:5,a:3}
#long=3
#{a:1,b:2,c:1}
#long=3
# if window[s[right]]>1:
#                 while left<len(s) and s[left]!=s[right]:
#                     window[s[left]]-=1
#                     if window[s[left]]==0:
#                         del window[s[left]]
#                     left+=1
#                 if left<len(s):
#                     window[s[left]]-=1
#                     left+=1
#                     right+=1
#             else:
#                 right+=1
#             longSub=max(longSub,right-left+1)