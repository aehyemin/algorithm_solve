class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        #최종 목적지를 반환하라
        start = set()
        end = set()
        for i in range(len(paths)):
            start.add(paths[i][0])
            end.add(paths[i][1])
        print(start, end)

        return (end - start).pop()
