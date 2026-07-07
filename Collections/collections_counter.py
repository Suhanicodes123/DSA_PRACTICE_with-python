Problem:collections.Counter()
Concept:Collections
Platform:HackerRank


from collections import Counter

x = int(input())
sizes = Counter(map(int, input().split()))

n = int(input())
money = 0

for _ in range(n):
    size, price = map(int, input().split())
    if sizes[size] > 0:
        money += price
        sizes[size] -= 1
print(money) 
