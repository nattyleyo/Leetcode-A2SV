class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        l = 0
        max_ = -1
        di = defaultdict(int)
        res = []
        n = len(s)
        for i in range(n):
            di[s[i]] = i
        for r in range(n):
            max_ =max(max_ , di[s[r]])
            if r == max_:
                res.append(r-l+1)
                l = r + 1
        return res
            