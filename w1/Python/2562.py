'''
문제
9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

예를 들어, 서로 다른 9개의 자연수

3, 29, 38, 12, 57, 74, 40, 85, 61

이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.

입력
첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.

출력
첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.

예제 입력 1 
3
29
38
12
57
74
40
85
61
예제 출력 1 
85
8
'''
max_n = 0
max_i = 0
for i in range(9) :
    n = int(input())
    if n > max_n :
        max_n = n
        max_i = i + 1
print(max_n)
print(max_i)


    








# range -->iterator 의 어떠한 배열
# list -> 저장된 A -> 해제
# iter -> [1,2,3,4..,9]

# first = []

# for i in range(9):
#     b = int(input())
#     first.append(b)
# second = sorted(first)

# print(second[-1], ) 
# print(first.index(second[-1])+1)


# for i in range(9):
#     b = int(input())
#     first.append(b)
# second = sorted(first)   
# print(second[8])

# # range(1,9) -> 1 <= range <9 1,2,3,4,5,6,7,8
# for i in range (9):
#     if second[8] == first[i]:
#         print(i+1)










