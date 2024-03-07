class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = [(intervals[i][0],i) for i in range(len(intervals)) ]
        starts.sort()
        ans = [-1]*len(starts)
        for i in range(len(starts)):
            low = 0
            high = len(starts)-1
            while low <= high:
                mid = (low + high)//2
                if starts[mid][0] >= intervals[i][1]:
                    ans[i] = starts[mid][1]
                    high = mid - 1
                else:
                    low = mid + 1
        # print(ans)
        return ans