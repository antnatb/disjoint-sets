import graph
import linked_list_disjoint_set
import disjoint_set_forest
import time
import matplotlib.pyplot as plt


def test_linked_list(graph, weighted, measurements):
    uf = linked_list_disjoint_set.UnionFind()
    total_time = 0
    for _ in range(measurements):
        start_time = time.time()
        uf.connected_components(graph, weighted)
        end_time = time.time()
        total_time += end_time - start_time
    average_time = total_time / measurements
    return average_time


def test_forest(graph, measurements):
    uf = disjoint_set_forest.UnionFind()
    total_time = 0
    for _ in range(measurements):
        start_time = time.time()
        uf.connected_components(graph)
        end_time = time.time()
        total_time += end_time - start_time
    average_time = total_time / measurements
    return average_time


def test_connected_components(density, measurements=10):
    dimensions = [500 * i for i in range(1, 11)]
    graphs = [graph.Graph(dim, density) for dim in dimensions]
    unweighted_times = [test_linked_list(g, False, measurements) for g in graphs]
    weighted_times = [test_linked_list(g, True, measurements) for g in graphs]
    forest_times = [test_forest(g, measurements) for g in graphs]
    plt.plot(dimensions, unweighted_times, label="Linked List (unweighted)")
    plt.plot(dimensions, weighted_times, label="Linked List (weighted)")
    plt.plot(dimensions, forest_times, label="Forest (path compression)")
    plt.title(f"Density: {density}")
    plt.xlabel("|V|")
    plt.ylabel("Time (s)")
    plt.legend()
    plt.show()


def test_proportional_density(measurements=10):
    dimensions = [500 * i for i in range(1, 11)]
    graphs = [graph.Graph(dim, 100 / dim) for dim in dimensions]
    unweighted_times = [test_linked_list(g, False, measurements) for g in graphs]
    weighted_times = [test_linked_list(g, True, measurements) for g in graphs]
    forest_times = [test_forest(g, measurements) for g in graphs]
    plt.plot(dimensions, unweighted_times, label="Linked List (unweighted)")
    plt.plot(dimensions, weighted_times, label="Linked List (weighted)")
    plt.plot(dimensions, forest_times, label="Forest (path compression)")
    plt.title(f"Density: 100/|V|")
    plt.xlabel("|V|")
    plt.ylabel("Time (s)")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    test_connected_components(0.01)
    test_proportional_density()

