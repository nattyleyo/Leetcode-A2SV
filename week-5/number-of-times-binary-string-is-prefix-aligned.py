class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count = 0
        max_flipped_index = 0 

        for i, flip in enumerate(flips, start=1):
            max_flipped_index = max(max_flipped_index, flip)
            
            if max_flipped_index == i:
                count += 1

        return count