class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive=timeToLive
        self.count_di={}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.count_di[tokenId] = currentTime + self.timeToLive

        
    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.count_di:
            if self.count_di[tokenId]>currentTime:
                self.count_di[tokenId] = currentTime + self.timeToLive
        
     
    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for token_time in self.count_di.values():
            if token_time > currentTime:
                count += 1
        return count
        
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)