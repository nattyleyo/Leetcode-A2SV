class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # my_set=set(nums1) & set(nums2)
        # if len(my_set)==0:
        #     return -1
        # return min(list(my_set))
        left=0
        right=0
        while left< len(nums1) and right<len(nums2):
            if nums1[left]<nums2[right]:
                left+=1
            elif nums1[left]>nums2[right]:
                right+=1
            else:
                return nums1[left]
        return -1
#4 5
#^
#1 2 3
#    ^