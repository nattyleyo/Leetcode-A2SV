class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        dic={}
        minlen=len(cards)
        for right in range(len(cards)):
            if cards[right] in dic:
                minlen=min(minlen, right-dic[cards[right]]+1)
            dic[cards[right]]=right 
        if len(set(cards))==len(cards):
            return -1
        return minlen