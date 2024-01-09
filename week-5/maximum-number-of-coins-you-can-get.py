class Solution:
    def maxCoins(self, piles: List[int]) -> int:
     
        piles.sort()
        answer = 0

        for i in range(len(piles) // 3, len(piles), 2):
            answer += piles[i]

        return answer