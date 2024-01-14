class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        my_sum=0
        left=0
        right=len(numbers)-1
        res=[]
        while left!=right:
            my_sum=numbers[left] + numbers[right]
            if my_sum > target:
                right-=1
            elif  my_sum < target:
                left+=1
            else:
                break
        res.append(left+1)
        res.append(right+1)
        return res
        