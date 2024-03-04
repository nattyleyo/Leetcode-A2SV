class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.min_unfair = float('inf')
        bucket = [0]*k
        def backtrack(idx,bucket):
            if idx >= len(cookies):
                self.min_unfair = min(self.min_unfair,max(bucket))
                return
            if max(bucket) > self.min_unfair:
                return
            for i in range(k):
                bucket[i] += cookies[idx]
                backtrack(idx + 1,bucket)
                bucket[i] -= cookies[idx]
        backtrack(0,bucket)
        return self.min_unfair