from bisect import bisect_right
n = int(input())
shop = list(map(int, input().split()))
shop.sort()
q = int(input())
coin = [0]*q
for i in range(q):
    coin[i] = int(input())
for i in range(q):
    print(bisect_right(shop, coin[i]))
