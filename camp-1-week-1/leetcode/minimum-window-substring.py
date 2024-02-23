class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = defaultdict(int)
        s_count = defaultdict(int)
        n = len(s)
        window = n
        left = 0
        right = 0
        res  = ''
        for i in range(len(t)):
            t_count[t[i]] += 1
        while right <n:
            s_count[s[right]] += 1
            # print(s_count)
            # print(t_count)
            while s_count and self.allCharsIn(t_count,s_count):
                if left >= n:
                    break
                if (len(res) == 0 or len(res) > right - left + 1):
                   res = s[left: right + 1]
                s_count[s[left]] -= 1
                if s_count[s[left]] == 0:
                    del s_count[s[left]]
                
                left += 1
            right += 1
        # return s[left:right+1]
        # print(window)
        return res
    def allCharsIn(self, t_count: dict, s_count: dict) -> bool:
        for char in t_count:
            if t_count[char] > s_count.get(char, 0):
                return False
        return True
