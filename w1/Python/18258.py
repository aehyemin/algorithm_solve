import sys
from collections import deque

N = int(input())

queue = deque()
def push(x):
    queue.append(x)


def pop() -> int:
    if not queue:
        return -1
    return queue.popleft()

def size() -> int:
    return len(queue)
        
def empty():
    if queue:
        return 0
    else:
        return 1

def front() :
    if not queue:
        return -1
    return queue[0]

def back():
    if not queue:
        return -1
    return queue[-1]

for i in range(N):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        push(int(order[1]))

    elif order[0] == 'pop':
        print(pop())
    
    elif order[0] == 'size':
        print(size())

    elif order[0] == 'empty':
        print(empty())
        
    elif order[0] == 'front':
        print(front())
        
    elif order[0] == 'back':
        print(back())
