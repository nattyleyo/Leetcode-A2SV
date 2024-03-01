class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        #using one score approach
        # left = 0
        # right = len(nums)-1
        # flag = 0
        # def helper(left,right):
        #     if left == right:
        #         return nums[left]
        #     leftScore = nums[left] - helper(left+1,right)
        #     rightScore = nums[right] - helper(left,right-1)
        #     return max(leftScore,rightScore)
        # flag = helper(left,right)
        # # print(flag)
        # if flag >= 0:
        #     return True
        # else:
        #     return False

        # using two score approach
        left = 0
        right = len(nums)-1
        turn = 1
        def helper(left,right,turn):
            if left == right:
                if turn:
                    return [nums[left],0]
                else:
                    return [0,nums[left]]
            if turn:
                leftScore = helper(left+1,right,not turn)
                rightScore = helper(left,right-1,not turn)

                leftScore[0] += nums[left]
                rightScore[0] += nums[right]

                if leftScore[0] > rightScore[0]:
                    return leftScore
                else:
                    return rightScore
            else:
                leftScore = helper(left+1,right,not turn)
                rightScore = helper(left,right-1,not turn)

                leftScore[1] += nums[left]
                rightScore[1] += nums[right]

                if leftScore[1] > rightScore[1]:
                    return leftScore
                else:
                    return rightScore
        x = helper(left,right,turn)
        # print(x)
        return True if x[0]-x[1] >= 0 else False
            