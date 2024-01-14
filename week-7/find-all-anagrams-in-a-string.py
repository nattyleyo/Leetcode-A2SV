class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        target = (Counter(p))
        window = (Counter(s[:k]))
        arr = []
        for i in range(k, len(s)):
            if target == window:
                arr.append(i-k)
            window[s[i-k]] -= 1
            if window[s[i-k]] == 0:
                del window[s[i-k]]
            window[s[i]] += 1
        if target == window:
            arr.append(len(s) - k)
            
        print(arr)
        return arr
