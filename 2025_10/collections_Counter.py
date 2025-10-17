
from collections import Counter

x = int(input())

size = list(map(int, input().split()))

inven = Counter(size)

n = int(input())

money = 0

for i in range(n):
    siz, dollar = map(int, input().split())
    if inven[siz] > 0:
        money += dollar
        inven[siz] -= 1
        
print(money)
