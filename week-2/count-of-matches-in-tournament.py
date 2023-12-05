class Solution:
    def numberOfMatches(self, n: int) -> int:
        match=0
        team=n
        while n>1:
            if n%2==0:
                match+=n/2
            else:
                match+=(n-1)/2
            n=team-match
        return int(match)
        