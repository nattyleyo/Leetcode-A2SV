class NumArray:
# -2  0   3   -5  2   -1
# -2  -2  1   -4  -2  -3
# 1,8,11,17,23
# 0,1,8,11,17,23
    def __init__(self, nums: List[int]):
        n = len(nums)
        self.pref=[0]*(n+1)
        for i in range(n):
            self.pref[i+1]=self.pref[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        mySum = self.pref[right+1] - self.pref[left]
        return mySum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)