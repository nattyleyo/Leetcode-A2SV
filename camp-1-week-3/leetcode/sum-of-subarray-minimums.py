class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        left = [1]*n
        stack = [(arr[0],1)]
        for i in range(1,n):
            while stack and arr[i] <= stack[-1][0]:
                left[i] += stack.pop()[1]
            stack.append((arr[i],left[i]))

        stack.clear()
        right = [1]*n
        stack = [(arr[-1],1)]
        for i in range(n-2,-1,-1):
            while stack and arr[i] < stack[-1][0]:
                right[i] += stack.pop()[1]
            stack.append((arr[i],right[i]))
        ans = 0

        for i in range(n):
            ans += arr[i]*left[i]*right[i]
        return ans%((10**9)+7)
