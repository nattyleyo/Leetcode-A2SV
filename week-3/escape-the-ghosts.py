class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        gh_turn=0
        di={}
        n=len(ghosts)
        my_turn=abs(target[0])+abs(target[1])
        for i in range(n):
            gh_turn= abs(target[0]-ghosts[i][0])+abs(target[1]-ghosts[i][1])
            di[i]=gh_turn
        minVal=min(di.values())
        if my_turn<minVal:
                return True
        return False

        