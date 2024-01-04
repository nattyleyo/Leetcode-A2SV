class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        my_set=set(nums1) & set(nums2)
        if len(my_set)==0:
            return -1
        return min(list(my_set))