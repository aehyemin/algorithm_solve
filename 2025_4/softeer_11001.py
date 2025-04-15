import sys
input = sys.stdin.readline
n = input()
arr = []
for i in range(int(n)):
    arr.append(input().strip())

for i in range(1, int(n)):
    for j in range(i):
        if "." in arr[i]:
            left, right = arr[i].split(".")
        else:
            left = arr[i]
            right = -1

        if "." in arr[j]:
            left_2, right_2 = arr[j].split(".")
        else:
            left_2 = arr[j]
            right_2 = -1

        if int(left) < int(left_2):
            arr[i], arr[j] = arr[j], arr[i]

        if int(left) == int(left_2):
            if int(right_2) > int(right):
                arr[i], arr[j] = arr[j], arr[i]

for i in arr:
    print(i)
