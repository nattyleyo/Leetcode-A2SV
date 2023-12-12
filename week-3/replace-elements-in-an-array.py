class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        di = {} 
        for i, num in enumerate(nums):
            di[num] = i
        n = len(operations)
        for i in range(n):
            remove = operations[i][0]
            add = operations[i][1]
            if remove in di:
                index = di[remove]
                nums[index] = add
                di.pop(remove) 
                di[add] = index 
        return nums