class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        #각자 빈도수가 다른가?
        hash = {}
        for i in arr:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1

        a = list(hash.values())
        

        for i in range(len(a)):
            for j in range(i):
                if a[i] == a[j]:
                    return False
        return True
                