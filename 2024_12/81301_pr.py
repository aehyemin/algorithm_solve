def solution(s):
    answer = ""
    i=0
    while i < len(s) :
        if s[i].isdigit():
            answer += s[i]
            i += 1
        elif s.startswith("zero", i):
            answer += "0"
            i += 4
        elif s.startswith("one", i):
            answer += "1"
            i += 3
        elif s.startswith("two", i):
            answer += "2"
            i += 3
        elif s.startswith("three", i):
            answer += "3"
            i += 5
        elif s.startswith("four", i):
            answer += "4"
            i += 4
        elif s.startswith("five", i):
            answer += "5"
            i += 4
        elif s.startswith("six", i):
            answer += "6"
            i += 3
        elif s.startswith("seven", i):
            answer += "7"
            i += 5
        elif s.startswith("eight", i):
            answer += "8"
            i += 5
        elif s.startswith("nine", i):
            answer += "9"
            i += 4
    return int(answer)