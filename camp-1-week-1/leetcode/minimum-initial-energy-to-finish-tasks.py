class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda task: task[1]-task[0])
        cur_min = tasks[0][1]
        total = 0
        print(tasks)
        for i in range(1,len(tasks)):
            if cur_min + tasks[i][0] >= tasks[i][1]:
                cur_min += tasks[i][0]
            else:
                cur_min = tasks[i][1]
        return cur_min
#[[10, 11], [8, 9], [1, 3], [2, 4], [10, 12]]
#cur=11
#total=19