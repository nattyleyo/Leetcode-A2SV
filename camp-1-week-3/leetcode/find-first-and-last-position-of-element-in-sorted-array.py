class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = -1
        n = len(nums)
        low = 0
        high = n-1
        #for the first occurence of no
        while low <= high:
            mid = (low + high)//2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                ans = mid
                high = mid - 1
        #for the last occurence of no
        res = [ans]
        ans = -1
        low = 0
        high = n-1
        while low <= high:
            mid = (low + high)//2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                ans = mid
                low = mid + 1
        res.append(ans)
        # print(res)
        return res