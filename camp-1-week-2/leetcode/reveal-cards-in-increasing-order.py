class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        queue = deque()
        n = len(deck)
        deck.sort(reverse=True)
        for i in range(n):
            if queue:
                next_top = queue.pop()
                queue.appendleft(next_top)
            queue.appendleft(deck[i])
        return queue
        

