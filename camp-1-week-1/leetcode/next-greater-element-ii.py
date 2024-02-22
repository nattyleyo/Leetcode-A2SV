class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        count = {}
        stack = []
        n = len(nums)
        for i in range(n):
            count[i] = -1
        i = 0
        c = 0
        while i < 2*n:
            if i == n:
                i = 0
                c +=1
            if c > 1:
                break
            while stack and stack[-1][1] < nums[i]:
                idx,val = stack.pop()
                count[idx] = nums[i]
            stack.append((i,nums[i]))
            i += 1
        # res =[val for val in count.values()]
        # print(count)
        return count.values()
