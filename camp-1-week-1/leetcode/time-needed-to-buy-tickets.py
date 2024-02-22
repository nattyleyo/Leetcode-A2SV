class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        queue = deque()
        for i,ticket in enumerate(tickets):
            queue.append((ticket,i))
        while queue:
            ticket,i = queue.popleft()
            count += 1
            ticket -= 1

            if ticket > 0:
                queue.append((ticket,i))
            if i == k and ticket == 0:
                break
        return count