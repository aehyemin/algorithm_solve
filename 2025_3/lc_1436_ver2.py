class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        #최종 목적지를 반환하라
        graph = {}
        for i in range(len(paths)):
            a = paths[i][0]
            b = paths[i][1]
            graph[a]= b

        end = paths[0][1]
        while end in graph:
            end = graph[end]
        return end
