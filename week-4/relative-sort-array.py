class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res=[]
        n=len(arr1)

        count_arr=[0]*(max(arr1)+1)
        my_list=list(set(arr1)-set(arr2))
        m=len(count_arr)
        for i in range(n):
            idx=arr1[i]
            count_arr[idx]+=1
        for i in range(len(arr2)):
            p=count_arr[arr2[i]]
            for j in range(p):
                res.append(arr2[i])
        if len(my_list)>0:
            tempIdx=min(my_list)
            for i in range(tempIdx,m):
                p=count_arr[i]
                if p>0 and i not in res:
                    for j in range(p):
                        res.append(i)
        return res



        