def solution(S):
    #올바른 문자열이면 1, 아니면 0 을 반환
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    stack = []
    for char in S:
        if char in '{[(':
            stack.append(char)
        else:
            if not stack:
                return 0
            tmp = stack.pop()
            if pairs[char] != tmp:
                return 0
    if not stack:
        return 1
    else:
        return 0
