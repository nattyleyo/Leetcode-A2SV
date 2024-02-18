class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        cur_sum = 0
        for i in range(len(arr)):
            cur_sum += arr[i]
            if i >= k-1:
                if  cur_sum >= (k * threshold):
                    count +=1
                cur_sum -= arr[i-(k-1)]
        return count