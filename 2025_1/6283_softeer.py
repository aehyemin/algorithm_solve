import sys

input = sys.stdin.readline

dct = list(map(int, input().split()))


if dct ==  [8, 7, 6, 5, 4, 3, 2, 1]:
    print("descending")
elif dct == [1, 2, 3, 4, 5, 6, 7, 8]:
    print("ascending")
else:
    print("mixed")