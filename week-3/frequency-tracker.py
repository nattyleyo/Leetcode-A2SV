class FrequencyTracker:
    def __init__(self):
        self.di = defaultdict(int)
        self.freq_di = defaultdict(int)

    def add(self, number: int) -> None:
        prev_freq = self.di[number]
        self.di[number] += 1
        cur_freq = self.di[number]
        self.freq_di[prev_freq] -= 1
        self.freq_di[cur_freq] += 1

    def deleteOne(self, number: int) -> None:
        if number in self.di:
            prev_freq = self.di[number]
            self.di[number] -= 1
            cur_freq = self.di[number]
            self.freq_di[prev_freq] -= 1
            if self.freq_di[prev_freq] == 0:
                del self.freq_di[prev_freq]
            if cur_freq > 0:
                self.freq_di[cur_freq] += 1
            else:
                del self.di[number]

    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.freq_di and self.freq_di[frequency] > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)