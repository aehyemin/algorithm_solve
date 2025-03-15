class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #매거진의 문자를 사용해서 구성될수 있으면 트루
        #문자는 한번씩만 사용할수있음
        for i in ransomNote:
            if i in magazine:
                #replace는 모든 문자를 제거함
                ransomNote = ransomNote.replace(i, "",1)
                magazine = magazine.replace(i, "",1)
       
        if ransomNote == "":
            return True
        else:
            return False



        