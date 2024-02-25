class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)
        left  = 0
        right  = 0
        n =len(fruits)
        window = 0
        while right < n:
            count[fruits[right]] += 1
            while len(count) > 2 :
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1
                # print(count)
            window = max( window, right-left+1)
            right += 1
        return window

