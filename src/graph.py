from collections import defaultdict
 
class Graph:
    def __init__(self,vertices):
        self.graph = defaultdict(list) 
        self.n_v = vertices 
        self.list_v = list(range(vertices))
    
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    def topologicalSortUtil(self,v,visited,stack):
 
        visited[v] = True
        name = self.list_v[v]

        for n in self.graph[name]:
            idx = self.list_v.index(n)
            if visited[idx] == False:
                self.topologicalSortUtil(idx,visited,stack)
                
        stack.insert(0,name)
 
    def topologicalSort(self):
        visited = [False]*self.n_v
        stack = []

        for i in range(self.n_v):
            if visited[i] == False:
                self.topologicalSortUtil(i,visited,stack)
 
        stack.reverse()
        return stack
