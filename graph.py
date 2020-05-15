

class Graph:
    """Directed graph data structure."""

    def __init__(self):
        self.nodes = set()

    def getNodeById(self, nodeId):
        for node in self.nodes:
            if node.id == nodeId:
                return node

    def addNodes(self, nodeIds):
        for nodeId in nodeIds:
            self.nodes.add(Node(nodeId))

    def addEdge(self, u, label, v):
        begin = self.getNodeById(u)
        end = self.getNodeById(v)

        begin.addEdge(label, end)

    def oneDepthTravel(self, begin, label):
        """return set of node-ids with one depth travel
        from the beginning with a specific label."""
        return Node.converToIdSet(self.getNodeById(begin).nextNodes(label))

    def travelOnLabel(self, begin, label):
        """return set of node-ids that reachable from node `begin` 
        by using `label` as many as posible."""
        result = self.getNodeById(begin).nextNodes(label)
        temp = set()
        while result != temp:
            temp = result.copy()
            for x in temp:
                result.update(x.nextNodes(label))
        return Node.converToIdSet(result)


class Node:
    """A data strucure for storing the nodes.
    Each node has id and a set that contain edges start from this node.
    """

    def __init__(self, id):
        self.id = id
        self.edges = set()

    def __str__(self):
        return self.id

    def addEdge(self, label, end):
        self.edges.add(Edge(self, label, end))

    def nextNodes(self, label):
        """Return a set of nodes exist a path to them with length one and specific label."""
        result = set()
        for edge in self.edges:
            if edge.label == label:
                result.add(edge.end)
        return result

    @classmethod
    def converToIdSet(cls, nodes):
        """Get set of nodes and return set of node's ids."""
        result = set()
        for node in nodes:
            result.add(node.id)
        return result


class Edge:
    """A data strucure for storing the edges."""

    def __init__(self, begin, label, end):
        self.begin = begin
        self.label = label
        self.end = end

    def __str__(self):
        return f'{self.begin.id} ---{self.label}---> {self.end.id}'
