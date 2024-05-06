import random


class Item:
    def __init__(self, value):
        # value of the item
        self.value = value
        # next item in the linked list
        self.next = None


class LinkedList:
    def __init__(self, item):
        # head and tail are the same for a new linked list
        self.head = item
        self.tail = item
        # size of the set
        self.size = 1


class UnionFind:
    def __init__(self):
        # dictionary to store the sets
        self.sets = {}

    def make_set(self, value):
        # create a new linked list with a single item
        item = Item(value)
        linked_list = LinkedList(item)
        # store the linked list in the dictionary
        self.sets[value] = linked_list

    def find(self, value):
        # return the head of the linked list
        return self.sets[value].head

    def union(self, u, v):
        # find head of v
        v_head = self.find(v)
        # find tail of u and v
        u_tail = self.sets[u].tail
        v_tail = self.sets[v].tail
        # set u tail next to v head
        u_tail.next = v_head
        # update tail of u to be tail of v
        self.sets[u].tail = v_tail
        # update size of u set
        self.sets[u].size += self.sets[v].size
        # delete v set
        del self.sets[v]
        # update all elements of v set to be u set
        current = v_head
        while current is not None:
            self.sets[current.value] = self.sets[u]
            current = current.next

    def weighted_union(self, u, v):
        if self.sets[u].size < self.sets[v].size:  # if u is smaller than v, swap them
            self.union(v, u)
        else:
            self.union(u, v)

    def connected_components(self, graph, weighted=False):
        # create a set for each node
        for u in graph.nodes:
            self.make_set(u)
        edges = []
        for u, neighbors in enumerate(graph.adjacency_list):
            for v in neighbors:
                if v > u:
                    edges.append((u, v))
        # shuffle the edges to make weighted union more likely to happen
        random.shuffle(edges)
        for u, v in edges:  # iterate over all edges
            if self.find(u) != self.find(v):
                if weighted:
                    self.weighted_union(u, v)
                else:
                    self.union(u, v)

    def print_connected_components(self):
        printed_lists = []
        for linked_list in self.sets.values():  # iterate over all sets
            current = linked_list.head
            if current not in printed_lists:  # avoid printing the same list twice
                printed_lists.append(current)
                while current is not None:
                    print(current.value, end='')
                    if current.next is not None:
                        print(' -> ', end='')
                    current = current.next
                print()
