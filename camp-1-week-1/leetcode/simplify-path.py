class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        li = list(map(str,path.split('/')))
        print(li)
        for p in li:
            if not p or p == '.':
                continue
            elif p == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        # print(stack)
        return '/' + '/'.join(stack)
            