class Solution:
    def frequencySort(self, s: str) -> str:
        hash = {}
        for i in s:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1

        has = sorted(hash.items(), key=lambda x:x[1], reverse=True)
        new_s = ""

        for i, val in enumerate(has):
            if val[1] >= 0:
                new_s += val[1]*val[0]
        return new_s