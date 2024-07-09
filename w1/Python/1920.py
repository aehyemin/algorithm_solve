def binary_search(original, exist, start, end):
    while start <= end : 
        mid = (start + end) // 2
        
        if original[mid] == exist:
            return mid
            
        elif original[mid] > exist:
            end = mid - 1
        # binary_search(original, exist, start, mid-1)
            
        else :
            start = mid + 1
        # binary_search(original, exist, mid+1, end)
    return None
    
N = int(input())
original =list(map(int,input().split()))
original.sort()

M = int(input())
exists =list(map(int,input().split()))

for exist in exists:
    result = binary_search(original, exist, 0, N-1)
    if result is not None:
        print("1")
    else:
        print("0")
