class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        my_dict1=defaultdict(int)
        my_dict2=defaultdict(int)
        set3=list(set(nums1)&set(nums2))
        res=[]
        for i in range(len(nums1)):
            my_dict1[nums1[i]]+=1
        for i in range(len(nums2)):
            my_dict2[nums2[i]]+=1
        for i in range(len(set3)):
            minVal=min(my_dict1[set3[i]],my_dict2[set3[i]])
            for j in range(minVal):
                res.append(set3[i])
        return res
        
