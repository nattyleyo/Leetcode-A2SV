class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        count = {}
        res = [0]*len(nums1)
        for i in range(len(nums1)):
            count[nums1[i]] = -1
        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                count[stack.pop()] = nums2[i]
            stack.append(nums2[i])
        print(count)
        for i in range(len(nums1)):
            res[i] = count[nums1[i]]
        # print(res)

        return res