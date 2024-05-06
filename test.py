import graph
import linked_list_disjoint_set
import time
import matplotlib.pyplot as plt


def test_linked_list(graph, weighted, measurements=5):
    uf = linked_list_disjoint_set.UnionFind()
    total_time = 0
    for _ in range(measurements):
        start_time = time.time()
        uf.connected_components(graph, weighted)
        end_time = time.time()
        total_time += end_time - start_time
    average_time = total_time / measurements
    return average_time


if __name__ == "__main__":
    dimensions = [500 * i for i in range(1, 11)]
    graphs = [graph.Graph(dim, 0.01) for dim in dimensions]
    unweighted_times = [test_linked_list(g, False, 10) for g in graphs]
    weighted_times = [test_linked_list(g, True, 10) for g in graphs]
    plt.plot(dimensions, unweighted_times, label="Unweighted")
    plt.plot(dimensions, weighted_times, label="Weighted")
    plt.xlabel("Number of nodes")
    plt.ylabel("Time (s)")
    plt.legend()
    plt.show()
