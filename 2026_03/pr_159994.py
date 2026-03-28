def solution(cards1, cards2, goal):
    if len(cards1) + len(cards2) < len(goal):
        return "No"
    
    one = 0
    two = 0
    for word in goal:
        if one < len(cards1) and word == cards1[one]:
            one += 1
        elif two < len(cards2) and word == cards2[two]:
            two += 1
        else:
            return "No"
    return "Yes"
