class Solution:
    def customSortString(self, order: str, s: str) -> str:
        #order 에 등장하는 것만 자리 고정, 나머지는 flex
        #order의 순서를 일단 따름
        #s가 order 안에 존재하면 출력
        new_word =""
        hash = {}
        for i in s:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1
        
        for i in order:
            if i in hash:
                new_word += hash[i] * i
            
        for i in s:
            if i not in order:
                new_word += i
        return new_word