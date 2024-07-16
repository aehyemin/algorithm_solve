# graph[node] : node와 연결된 node의 리스트 라고 가정할때
def dfs(graph, start_node):
    visit = list()
    stack = list()
    
    stack.append(start_node)
    
    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])
            
        return visit