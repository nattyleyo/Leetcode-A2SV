class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        di = defaultdict(int)
        temp1 = []
        temp2 = []
        ans=[]
        for match in matches:
            for player in range(2):
                key= match[player]
                if player==1:
                    di[key] += 1
                else:
                    di[key]+=0
        for player in di:
            if di[player] == 0:
                temp1.append(player)
            elif di[player] == 1:
                temp2.append(player)
        ans.append(sorted(temp1))
        ans.append(sorted(temp2))
        return ans