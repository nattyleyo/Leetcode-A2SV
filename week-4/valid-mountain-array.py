class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        p=0
        n=len(arr)
        max_idx=arr.index(max(arr))
        if n<3:
            return False
        if max_idx==n-1 or max_idx==0:
            return False
        while p <=max_idx-1:
            if arr[p]<arr[p+1]:
                p+=1
            else:
                return False
        p=max_idx
        while p < n-1:
            if arr[p]>arr[p+1]:
                p+=1
            else:
                return False
        return True