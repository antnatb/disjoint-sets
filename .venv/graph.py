import random

class Graph:
    def __init__(self, num_nodes, density):
        if density < 0 or density > 1:
            raise ValueError("Density must be between 0 and 1")
        self.nodes = [i for i in range(num_nodes)]
        self.adjacency_list = [[] for _ in range(num_nodes)]
        max_edges = num_nodes * (num_nodes - 1) // 2
        num_edges = int(density * max_edges)
        edges_generated = 0
        while edges_generated < num_edges:
            node1 = random.choice(self.nodes)
            node2 = random.choice(self.nodes)
            if node1 != node2 and node2 not in self.adjacency_list[node1]:
                self.adjacency_list[node1].append(node2)
                self.adjacency_list[node2].append(node1)
                edges_generated += 1
    def print_edges(self):
        n_edges = 0
        for node, neighbors in enumerate(self.adjacency_list):
            for neighbor in neighbors:
                if neighbor > node:
                    print(f"({node}, {neighbor})")
                    n_edges += 1
        print (f"Total number of edges: {n_edges}")


