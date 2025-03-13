class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #문자열을 정렬해서 확인
        #directory.values()
#정렬한 문자열을 해시맵의 키(key),
#해당 키에 해당하는 값을 원래 문자열들의 리스트로 저장
#최종 결과는 해시맵에 저장된 모든 리스트
        #sort는 문자열 자체를 정렬하진 못함
        #sorted 를 사용해야함
        dict = {}
        for s in strs:

            key = ''.join(sorted(s))
            print(key)

            if key in dict:
                dict[key].append(s)
            else:
                dict[key] = [s]

        return list(dict.values())