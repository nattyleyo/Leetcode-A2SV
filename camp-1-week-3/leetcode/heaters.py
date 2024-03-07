class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        ans = [1]*len(houses)
        heaters.sort()
        n = len(heaters)
        maxi = float('-inf')
        for i in range(len(houses)):
            low = 0
            high = n - 1
            mid = 0
            mini = float('inf')
            while low <= high:
                mid = (low + high)//2
                if houses[i] >= heaters[mid]:
                    mini = min(mini,abs(houses[i]-heaters[mid]))
                    low = mid + 1
                else:
                    mini = min(mini,abs(houses[i]-heaters[mid]))
                    high = mid - 1
            maxi = max( maxi, mini)
        return maxi           