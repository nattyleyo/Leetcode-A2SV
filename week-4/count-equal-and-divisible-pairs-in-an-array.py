class Solution:
  def countPairs(self, nums: List[int], k: int) -> int:
    ans = 0
    my_di = defaultdict(list)

    for i, num in enumerate(nums):
      my_di[num].append(i)

    for idx in my_di.values():
      gcds = collections.Counter()
      for i in idx:
        gcd_i = math.gcd(i, k)
        for gcd_j, count in gcds.items():
          if gcd_i * gcd_j % k == 0:
            ans += count
        gcds[gcd_i] += 1

    return ans