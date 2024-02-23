class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        while target > 1 and maxDoubles > 0:
            if target % 2 == 0:
                count += 1 
            else:
                count += 2 
            target //= 2
            maxDoubles -= 1
        return count + target -1