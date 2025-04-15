import sys
input = sys.stdin.readline
n = input()
arr = []
for i in range(int(n)):
    arr.append(input().strip())

def custom_key(str_num):
    if "." in str_num:
        left, right = str_num.split(".")
        return (int(left),1,int(right))
    else:
        return (int(str_num),0,0)
        
arr.sort(key=custom_key)
for i in arr:
    print(i)