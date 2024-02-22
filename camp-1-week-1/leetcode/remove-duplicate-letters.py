class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = defaultdict(int)
        stack = []
        my_set = set()
        for i in range(len(s)):
            count[s[i]] += 1
        for i in range(len(s)):
            if s[i] not in my_set:
                while stack and stack[-1] >= s[i] and count[stack[-1]] > 1:
                    count[stack[-1]] -= 1
                    popped = stack.pop()
                    my_set.remove(popped)
            # if stack[-1] in count:
                stack.append(s[i])
                my_set.add(s[i])
            else:
                count[s[i]] -= 1
        # if s.count(stack[-1]) > 1 and count[stack[-1]] > 1: 
        #     stack.pop()
        # print(count)
        # print(stack)
        return ''.join(stack)