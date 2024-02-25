class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        left = 0
        n = len(nums)
        my_set = set(nums)
        my_di = defaultdict(int)
        count = 0
        for right in range(n):
            my_di[nums[right]] += 1
            while len(my_di) == len(my_set) and left <= right:
                my_di[ nums[left] ] -= 1

                if my_di[nums[left]] == 0:
                    del my_di[ nums[left] ]
                left += 1
                count += n - right
        return count
            
                