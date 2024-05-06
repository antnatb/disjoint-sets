import random


class Node:
    def __init__(self, value):
        self.value = value
        self.parent = self


class UnionFind:
    def __init__(self):
        # dictionary to store the nodes
        self.nodes = {}

    def make_set(self, value):
        # create a new node
        node = Node(value)
        # store the node in the dictionary
        self.nodes[value] = node

    def find(self, value):
        # find the node with the given value
        u = self.nodes[value]
        # path compression
        if u != u.parent:                        # not the root?
            u.parent = self.find(u.parent.value)  # the root becomes the parent
        return u.parent                          # return the root

    def union(self, u, v):
        u_root = self.find(u)
        v_root = self.find(v)
        v_root.parent = u_root

    def connected_components(self, graph):
        for u in graph.nodes:
            self.make_set(u)
        edges = []
        for u, neighbors in enumerate(graph.adjacency_list):
            for v in neighbors:
                if v > u:
                    edges.append((u, v))
        random.shuffle(edges)
        for u, v in edges:
            if self.find(u) != self.find(v):
                self.union(u, v)

    def print_connected_components(self):
        components = {}
        for u in self.nodes:
            root = self.find(u)
            if root.value not in components:
                components[root.value] = []
            components[root.value].append(u)
        for root, nodes in components.items():
            print(f"Component with root {root}: {nodes}")


