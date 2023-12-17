class Bitset:
    def __init__(self, size: int):
      self.my_set = ['0'] * size  # the original
      self.rev_set= ['1'] * size  # the reversed
      self.ones = 0
      self.size=size
    
    def fix(self, idx: int) -> None:
      if self.my_set[idx] == '0':
        self.ones += 1
      self.my_set[idx] = '1'
      self.rev_set[idx] = '0'
    
    def unfix(self, idx: int) -> None:
      if self.my_set[idx] == '1':
        self.ones -= 1
      self.my_set[idx] = '0'
      self.rev_set[idx] = '1'
    
    def flip(self) -> None:
      self.my_set, self.rev_set = (self.rev_set, self.my_set)
      self.ones = self.size - self.ones
    
    def all(self) -> bool:
      return self.ones == len(self.my_set)
    
    def one(self) -> bool:
      return self.ones
    
    def count(self) -> int:
      return self.ones
    
    def toString(self) -> str:
      return ''.join(self.my_set)

# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()