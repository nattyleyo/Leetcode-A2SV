class OrderedStream:

    def __init__(self, n: int):
        self.n=n
        self.res=[None]*n
        self.ptr=0
    def insert(self, idKey: int, value: str) -> List[str]:
        self.res[idKey-1]=value
        ans=[]
        while self.ptr<len(self.res) and self.res[self.ptr]!=None:
            ans.append(self.res[self.ptr])
            self.ptr+=1
        return ans

        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)