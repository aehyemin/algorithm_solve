# import sys
# input = sys.stdin.readline

# formula = input().split('-')

# for index, num in enumerate(formula):
#     if '+' in num:
#         sum_result = sum(map(int, num.split('+')))
#         formula[index] = sum_result
        
# # print(sum_result)      
# re_result = int(formula[0])

# for k in formula[1:]:
#     re_result -= int(k)
# print(re_result)

formula = input().split('-')
new = []
for i in formula :
    new.append(sum(list(map(int, i.split('+')))))

for j in new[1:]:
    new[0] -= j
    
print(new[0])

    