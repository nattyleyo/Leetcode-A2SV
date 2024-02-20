class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        total = numOnes + numZeros
        remainder = total - k
        if k <= numOnes:
            return k
        elif k > numOnes and (k < total or k == total):
            return numOnes
        elif k > total:
            return numOnes + remainder
        