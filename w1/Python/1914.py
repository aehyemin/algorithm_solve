n =  int(input())
def movement(n:int, start:int, end:int):
    
    if n == 1 :
        print(start,end)
        return
    
    
    else :
        movement(n-1, start, 6-start-end)
        print(start,end)
        movement(n-1, 6-start-end, end)

if n <=20 : 
    print(2**n-1)
    movement(n,1,3)

else:
    print(2**n-1)

# print(2**n-1)
# movement(n,1,3)


