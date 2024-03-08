class TimeMap:

    def __init__(self):
        self.dic = defaultdict(list)

        # self.time = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # self.arr.append((key,value,timestamp))
        self.dic[key].append((value,timestamp))
        # self.time[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key in self.dic:
            n = len(self.dic[key])
            low = 0
            high = n-1
            ans = 0
            
            if timestamp < self.dic[key][0][1]:
                return ''

            while low <= high:
                mid = (low + high)//2
                if self.dic[key][mid][1] > timestamp:
                    high = mid - 1
                else:
                    ans = mid
                    low = mid + 1
            return self.dic[key][ans][0]
        else:
            return ''


        #another approach using bisectright
    
        # idx = bisect_right(self.time[key],timestamp)
        # return self.dic[key][idx-1][0] if idx else ''

        



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
