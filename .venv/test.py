import graph
import linked_list_disjoint_set
import time
import matplotlib.pyplot as plt

def test_linked_list(graph, weighed, measurements = 5):
    uf = linked_list_disjoint_set.UnionFind()
    total_time = 0
    for _ in range(measurements):
        start_time = time.time()
        uf.connected_components(graph, weighed)
        end_time = time.time()
        total_time += end_time - start_time
    average_time = total_time / measurements
    return average_time


if __name__ == "__main__":
    dimensions = [300 * i for i in range(1, 11)]
    graphs = [graph.Graph(dim, 0.01) for dim in dimensions]
    unweighed_times = [test_linked_list(g, False, 10) for g in graphs]
    weighed_times = [test_linked_list(g, True, 10) for g in graphs]
    plt.plot(dimensions, unweighed_times, label="Unweighed")
    plt.plot(dimensions, weighed_times, label="Weighed")
    plt.xlabel("Number of nodes")
    plt.ylabel("Time (s)")
    plt.legend()
    plt.show()





