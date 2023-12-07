class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        dif=right-left
        my_set=set()
        for i in range(len(ranges)):
          start=ranges[i][0]
          end= 1+ ranges[i][1]
          for j in range(start,end):
            my_set.add(j)
        for i in range(left,right+1):
            if not (i in my_set):
              return False
        return True
      



        