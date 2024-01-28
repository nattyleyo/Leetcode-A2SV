class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        M, N = len(firstList), len(secondList)
        i = j = 0
        res = []

        while i < M and j < N:
            l1, l2 = firstList[i], secondList[j]
            start = max(l1[0], l2[0])
            end = min(l1[1], l2[1])

            if start <= end:
                res.append([start, end])
    
            if l1[1] < l2[1]:
                i += 1
            else:
                j += 1
        
        return res