
from collections import deque
class GraphAl:
    
    def __init__(self, size):
        self.size = size
        self.lista = [[] for i in range(size)]

    def __repr__(self):
        return '{}'.format(self.lista)

    def getWeight(self, source, destination):
        for d in self.lista[source]:
            if d[0] == destination:
                return d[1]

    def addArc(self, source, destination, weight):
        self.lista[source].append((destination, weight))

    def getSuccessors(self, vertice):
        succs = []
        for d in self.lista[vertice]:
            succs.append(d[0])
        return succs

def hayCaminoDFS(g, i, f):
    q = deque() # Java Stack()
    q.append(i)
    while( len(q) != 0 ):
        n = q.pop()
        if (n == f):
            return True
        for hijito in g.getSuccessors(n):
            q.append(hijito)
    return False
def hayCaminoBFS(g, i, f):
    q = deque() # Java Queue()
    q.appendLeft(i)
    while( len(q) != 0 ):
        n = q.pop()
        if (n == f):
            return True
        for hijito in g.getSuccessors(n):
            q.appendLeft(hijito)
    return False
    

ga = GraphAl(5)
ga.addArc(0, 3, 10)
print(ga)
print(ga.getWeight(0, 3))
ga.addArc(0, 4, 7)
print(ga)
print(ga.getSuccessors(0))
print(hayCaminoDFS(ga,0,4))



