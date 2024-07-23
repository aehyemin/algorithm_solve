# - 다음에 + 가 있으면 마이너스를 제외하고 더해준다
# - 다음에 + 가 잇으면 계속 더해준다

formula = (input().split('-')) 

for index, num in enumerate(formula):
    if "+" in num:
        sum_result = sum(map(int,num.split("+")))
        formula[index] = str(sum_result)

re_result = int(formula[0])         

for j in formula[1:]:
    re_result -= int(j)
print(re_result)


# a = input().split('-')

# x=[]

# for i in a:

#     x.append(sum(list(map(int,i.split('+')))))

# for i in range(1,len(x)):
    
#     x[0] -= x[i]

# print(x[0])


# import sys
# if __name__ == "__main__":

#     string = input()
#     minus_split = string.split("-")
    
#     # print(minus_split)
    
#     if len(minus_split) == 1:
#         sum1 = 0
#         p_split = minus_split[0].split("+")
#         for i in p_split:
#             sum1 += int(i)
#         print(sum1)
#     else:
#         sum = int(minus_split[0])
#         for i in minus_split[1:]:
#             p_split = i.split("+")
#             p_sum = 0
#             for j in p_split:
#                 p_sum += int(j)
#             sum -= p_sum
#         print(sum)