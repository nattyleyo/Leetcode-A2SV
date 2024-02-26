class Solution:
    def myFunc(self, s: List[str],start:int,end:int):
        if start == end//2:
            return
        if start != end - start -1:
            s[start],s[end-start-1]=s[end-start-1],s[start]
        self.myFunc( s,start +1 ,end)


    def reverseString(self, s: List[str]) -> None:
        """
        Modifies the input list in-place to reverse its elements using recursion.
        """  
        start = 0
        end = len(s)
        self.myFunc( s,start,end )
        