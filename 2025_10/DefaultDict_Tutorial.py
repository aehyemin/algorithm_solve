from collections import defaultdict

n, m = map(int, input().split())

n_word = defaultdict(list)

for i in range(n):
    n_word[input()].append(i+1)
    

for j in range(m):
    hey = input()
    if hey in n_word:
        print(" ".join(map(str, n_word[hey])))
