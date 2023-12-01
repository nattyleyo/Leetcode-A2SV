class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num%3!=0:
            return []
        else:
            b=num/3
            a=b-1
            c=b+1
            arr=[int(a),int(b),int(c)]
            return arr