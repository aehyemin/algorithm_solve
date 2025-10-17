from collections import Counter
n = int(input())

arr = []
for i in range(n):
    arr.append(input())
    
word = Counter(arr)

print(len(word))
word_score = list(word.values())
print(" ".join(map(str, word_score)))
