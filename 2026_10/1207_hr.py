class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        oc = {}
        for i in range(len(arr)):
            if arr[i] not in oc:
                oc[arr[i]] = 1
            else:
                oc[arr[i]] += 1
        
        val = oc.values()
        if len(set(val)) == len(val):
            return True
        return False
        
