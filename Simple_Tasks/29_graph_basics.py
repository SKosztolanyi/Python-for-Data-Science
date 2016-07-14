class Node(object):
    def __init__(self, name):
        self.name = str(name)
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self, src, dest):
        # src and dest will be Nodes
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return str(self.src) + '->' + str(self.dest)

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight = 1.0):
        self.src = src
        self.dest = dest
        self.weight = weight
    def getWeight(self):
        return self.weight
    def __str__(self):
        return str(self.src) + '->(' + str(self.weight) + ')'\
            + str(self.dest)
            

# adding a new class of Edge
class WeightedEdge2(Edge):
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight
        pass
    def getWeight(self):
        # Your code here
        return self.weight
    def __str__(self):
        return str(self.src) + '->' + str(self.dest) +' (' + str(self.weight) + ')'
            
            
class Digraph(object): 
    # building a one directional graph
    def __init__(self):
        self.nodes = set([])
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = res + str(k) + '->' + str(d) + '\n'
        return res[:-1]

class Graph(Digraph):
    # It is an extension of Diagraph
    # Graph can have more than one edge and can go both ways
    def addEdge(self, edge):
        Digraph.addEdge(self, edge) # adds an edge
        rev = Edge(edge.getDestination(), edge.getSource()) # gets an opposite direction of edge
        Digraph.addEdge(self, rev) # adds also the opposite direction


def printPath(path):
    # a path is a list of nodes
    result = ''
    for i in range(len(path)):
        if i == len(path) - 1:
            result = result + str(path[i])
        else:
            result = result + str(path[i]) + '->'
    return result


nodes = []
nodes.append(Node('ABC')) # nodes[0]
nodes.append(Node('ACB')) # nodes[1]
nodes.append(Node('BAC')) # nodes[2]
nodes.append(Node('BCA')) # nodes[3]
nodes.append(Node('CAB')) # nodes[4]
nodes.append(Node('CBA')) # nodes[5]

print nodes

g = Graph()
for n in nodes:
    g.addNode(n)
#        
#edges = []
#edges.append(Edge('ABC', 'ACB'))
#edges.append(Edge('ABC', 'BAC'))
#edges.append(Edge('BCA', 'BAC'))
#edges.append(Edge('CAB', 'CBA'))
#edges.append(Edge('CBA', 'BCA'))
#
#for e in edges:
#    g.addEdge(e)
    # this solution is not working and raising value error: Node not in graph.


#Correct solution:
    # I have to represent to nodes in indexes and not in their names:
    
#When you are using .getName() you are just getting the string representation of the node object, not actually the node.
#The Node is a class, so when you are asking it if it has the node, 
#it is looking for the object Node, not just a string, which is what you are currently testing for.

g.addEdge(Edge(nodes[0], nodes[1]))
g.addEdge(Edge(nodes[0], nodes[2]))
g.addEdge(Edge(nodes[1], nodes[4]))
g.addEdge(Edge(nodes[2], nodes[3]))
g.addEdge(Edge(nodes[5], nodes[4]))
g.addEdge(Edge(nodes[5], nodes[3]))
# Each node has two possible connections
# The connections go both ways, there are 6 possible double sided connections

