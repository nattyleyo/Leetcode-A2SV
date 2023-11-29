class Solution:
    def convertTemperature(self, cel: float) -> List[float]:
        kel=cel+273.15
        fahr=cel*1.80+32
        ans=[kel,fahr]
        return ans
        