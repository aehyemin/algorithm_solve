class Solution:
    def repeatedCharacter(self, s: str) -> str:
        #문자열을 한번만 순회하면서, 등장한 문자를 SET 에 저장
        #시간 복잡도 O(N), 공간복잡도 O(1) 또는 O(M)

        #처음으로 두번 반복된 알파벳을 출력
        dict = {}
        for char in s:
            if char not in dict:
                dict[char] = 1 # 초기값을 지정
            else:
                dict[char] += 1
                if dict[char] == 2:
                    return char