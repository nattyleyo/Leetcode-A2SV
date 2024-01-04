class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n=len(skill)
        left=0
        right=n-1
        tempSum=0
        chem = skill[left] + skill[right]
        print(skill)
        while left<right:
            if skill[left]+skill[right]!=chem:
                return -1
            tempSum += skill[left] * skill[right]
            left+=1
            right-=1
        return tempSum
        