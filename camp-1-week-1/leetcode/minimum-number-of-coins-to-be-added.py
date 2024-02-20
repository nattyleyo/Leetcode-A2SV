class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        res = 0
        max_ = 0
        r = 0
        coins.sort()
        while max_ < target:
            if r < len(coins) and coins[r] <= max_ + 1:
                max_ += coins[r]
                r += 1
            else:
                add = max_ + 1
                max_ += add
                res += 1
        return res
#1  4   10  5   7   19
#       ^
#max=7
#1~7
#tar=19
#[2,8]