# Enter your code here. Read input from STDIN. Print output to STDOUT
# lower >> upper >> odd >> even

s = input()

#al, num arr distinct
u_al = []
l_al = []
odd = []
even = []

for i in s:
    if i.isupper():
        u_al.append(i)
    elif i.islower():
        l_al.append(i)
    elif i.isdigit():
        if int(i) % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

u_al.sort()
l_al.sort()
odd.sort()
even.sort()
new = l_al + u_al + odd + even

print("".join(new))
