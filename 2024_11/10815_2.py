#이분탐색 풀이
#숫자카드 N개, 정수 M개

def binary_search(arr, goal):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left+right) // 2
        if arr[mid] == goal:
            return True
        elif arr[mid] < goal:
            left = mid + 1
        else:
            right = mid - 1
             


N = int(input()) #상근이가 가진 숫자 카드 개수
number = list(map(int, input().split())) #숫자 카드에 적혀있는 정수
number.sort()

M = int(input())
find_num = list(map(int, input().split()))

ans=[]
for num in find_num:
    if binary_search(number, num):
        ans.append(1)
    else:
        ans.append(0)
print(' '.join(map(str, ans)))

