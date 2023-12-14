class Solution:
    def minimizedStringLength(self, s: str) -> int:
        n=len(s)
        my_set=set()
        # if n<2:
        #     return 1
        for i in range(n):
            if s[i] not in my_set:
                my_set.add(s[i])
        m=len(my_set)
        return m




        