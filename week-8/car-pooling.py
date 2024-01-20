class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        arr=[0]*(max(to[2] for to in trips)+1)
        pref=0
        for i in range(len(trips)):
            arr[trips[i][1]] += trips[i][0]
            arr[trips[i][2]] -= trips[i][0]
        for i in range(len(arr)):
            pref+=arr[i]
            if pref > capacity:
                return False
        return True









#1  2   3   4   5   6   7
#2              -2
#       3              -3
#2  0   3  0   -2  0   -3
#2  2   5  5    3  3    0