def solution(sizes):
    #정렬했을때 sizes[0], size[1] 에서 각각 가장 큰 길이를 뽑음
    for i in sizes:
        i.sort()
    print(sizes)
    
#     max_one = 0
#     max_two = 0
    
#     for j in sizes:
#         if max_one < j[0]:
#             max_one = j[0]
#         if max_two < j[1]:
#             max_two = j[1]
    max_one = max(x[0] for x in sizes)
    max_two = max(x[1] for x in sizes)
    
    
    return max_one * max_two
    
