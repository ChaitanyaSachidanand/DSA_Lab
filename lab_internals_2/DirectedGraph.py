
# a={}
# a.setdefault()
import sys

Max_Size_cost=sys.maxsize
min_size_cost=0
class DirectedGraph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def add_node(self, node_name):
        self.nodes[node_name] = []

    # def add_edge(self, edge_name, cost):
    def add_edge(self, edge_name, start_node, end_node, cost):
        edge = {'edge_name': edge_name, 'start_node': start_node, 'end_node': end_node, 'cost': cost}
        # self.edges[start_node]=[].append(edge)
        self.edges.setdefault(start_node, []).append(edge)

    def get_minimum_cost_edge(self):
        min_edge = None
        # min_cost = 1000000
        min_cost= Max_Size_cost
        for edges in self.edges.values():
            #[lamda x: x in edges.values()]
            for edge in edges:
                if edge['cost'] < min_cost:
                    min_edge = edge['edge_name']
                    min_cost = edge['cost']
        return min_edge, min_cost

    def get_maximum_cost_edge(self):
        #cost of max finding 
        max_edge = None
        max_cost = min_size_cost
        for edges in self.edges.values():
            #by default nothing
            for edge in edges:
                if edge['cost'] > max_cost:
                    max_edge = edge['edge_name']
                    max_cost = edge['cost']
        return max_edge, max_cost
    
# Initialize thew DirectedGraph
graph = DirectedGraph()

# creating and adding the nodes
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")
graph.add_node("E")

# Adding the Directed graphs edges with their start and end nodes with weights of edges
graph.add_edge("Edge1", "A", "B", 20)
graph.add_edge("Edge2", "B", "C", 10)
graph.add_edge("Edge3", "C", "A", 5)
graph.add_edge("Edge4", "C", "D", 30)
graph.add_edge("Edge5", "D", "E", 20)
graph.add_edge("Edge6", "D", "A", 40)
graph.add_edge("Edge7", "E", "A", 100)

# min cost edge
min_edge, min_cost = graph.get_minimum_cost_edge()
print("Minimum costing edge: ",min_edge," Cost: ",min_cost)

#  max cost edge
max_edge, max_cost = graph.get_maximum_cost_edge()
print("Maximum cost ofedge: ",max_edge," Cost: ",max_cost)