class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        min_rab = 0
        total = 0
        for key in count:
            min_rab = ceil(count[key]/(key +1))
            min_rab *= (key +1)
            total += min_rab
            # print(min_rab)
        return total
#1  1   2
#{1:2,2:1}
# ^3
