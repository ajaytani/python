# master list of vertices in Graph and each vertex

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    def __str__(self):
        return str(self.id) + ' connected to: ' + str([x.id for x in self.connectedTo])


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def addEgdge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)

        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

    def __contains__(self, item):
        return item in self.vertList

def bfs(adj, s):
    level = {s:0}
    parent = {s:None}
    i =1
    frontier = [s]
    visited = [(s,None,0)]
    while frontier:
        nextlist = []
        print ('level : ',i)
        for u in frontier:
            for v in adj[u]:
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    nextlist.append(v)
                    visited.append((v,u,i))
        frontier = nextlist
        i += 1
    return visited

def bfs2(graph,start):
    visited, queue = set(), [start]
    while queue:
        print(queue)
        print(visited)
        vertex = queue.pop()
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)

    return visited



graph = { 'A': set(['B','C']),
          'B': set(['A','D','E']),
          'C': set(['A','F']),
          'D': set(['B']),
          'E': set(['B', 'F']),
          'F': set(['C','E'])
          }

print (bfs(graph,'A'))
print(bfs2(graph,'A'))

#
# x = Graph()
# for i in range(5):
#     x.addVertex(i)
#
# for i in range(2,5,2):
#     x.addEgdge(i,i-1,i*(i-1))
#
# for vertex in x:
#     print vertex
#     print vertex.getConnections()
#     print ('\n')
#
