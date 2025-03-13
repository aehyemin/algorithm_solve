class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            # 26개의 영문 소문자에 대한 개수를 저장할 리스트 초기화
            count = [0] * 26
            # 각 문자에 대해 해당하는 인덱스의 값을 1씩 증가
            for char in s:
                count[ord(char) - ord('a')] += 1
            # count 리스트를 튜플로 변환하여 해시맵의 키로 사용

            key = tuple(count)

            if key in anagrams:
                anagrams[key].append(s)
            else: 
                anagrams[key] = [s]
        return list(anagrams.values())
