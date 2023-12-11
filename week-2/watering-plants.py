class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        step=0
        leftW = 0
        for i, plant in enumerate(plants):
            if leftW < plant:
                step += 2*i
                leftW = capacity
            step += 1
            leftW -= plant 
        return step