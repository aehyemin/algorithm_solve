height_list = []
extract_list = []


for _ in range(9):
    height_list.append(int(input()))


height_sum = sum(height_list)

for i in range(9):
    for j in range(i+1,9):
        if height_sum - height_list[i] - height_list[j] == 100:
            extract_list.append(height_list[i])
            extract_list.append(height_list[j])
            break
    if extract_list:
        break

for i in sorted(height_list):
    if i not in extract_list:
        print(i)

