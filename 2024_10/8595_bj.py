N = input()

number = input()
total = 0
#print(number)
real_num = []
current_num = ''
#숫자 뒤에 숫자면 합친다
for char in number:
    if char.isdigit():
        current_num += char
    else:
        if current_num:
            real_num.append(current_num)
            current_num =''

if current_num:
    real_num.append(current_num)
    
for num in real_num :
    total += int(num)
print(total)
                
        
