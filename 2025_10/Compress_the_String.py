from itertools import groupby

s = input()
result = []
for key, group in groupby(s):
    result.append((len(list(group)), int(key)))
print(' '.join(map(str, result)))


from itertools import groupby

s = input()
result = []
for key, group in groupby(s):
    result.append(f"({len(list(group))}, {key})")
    
print(' '.join(result))
