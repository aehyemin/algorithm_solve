from collections import deque
import sys

N = int(input())

stack = deque()

for i in range(N):
    order = list(sys.stdin.readline().split())

    if order[0] == 'push':
        stack.append(order[1])

    elif order[0] == 'pop':
        if len(stack) != 0:
            n = stack.pop()
            print(n)
        else: print(-1)

    elif order[0] == 'size':
        print(len(stack))

    elif order[0] == 'empty':
        if len(stack) == 0:
            print("1")
        else : 
            print("0")
        
    elif order[0] == 'top':
        if len(stack) != 0:
            print(stack[-1])
        else: 
            print(-1)




    


    # def __init__(self, maxlen: int = 256) -> None:
    #     self.capacity = maxlen
    #     self.__stk = deque([],maxlen)

    # def push(self, value: Any) -> None:
    #     self.__stk.append(value)

    # def pop(self) -> Any:
    #     return self.__stk.pop()


    # def __size__(self) -> int:
    #     return len(self.__stk)
    
    # def empty(self) -> bool:
    #     try :
    #         if not self.__stk:
    #             return 1
    #     except ValueError:
    #         return 0
     
    # def top(self) -> Any:
    #     try: 
    #         return self.__peek(-1)
    #     except ValueError:
    #         return -1
        