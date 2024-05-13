import graph
import linked_list_disjoint_set
import disjoint_set_forest
import time
import matplotlib.pyplot as plt


def test_linked_list_time(graph, weighted, measurements):
    uf = linked_list_disjoint_set.UnionFind()
    total_time = 0
    for _ in range(measurements):
        start_time = time.time()
        uf.connected_components(graph, weighted)
        end_time = time.time()
        total_time += end_time - start_time
    average_time = total_time / measurements
    return average_time


def test_forest_time(graph, measurements):
    uf = disjoint_set_forest.UnionFind()
    total_time = 0
    for _ in range(measurements):
        start_time = time.time()
        uf.connected_components(graph)
        end_time = time.time()
        total_time += end_time - start_time
    average_time = total_time / measurements
    return average_time


def compare_all_running_times(edges_nodes_ratio, step=500, measurements=5):
    dimensions = [step * i for i in range(1, 11)]
    graphs = [graph.Graph(dim, edges_nodes_ratio * dim) for dim in dimensions]
    unweighted_times = [test_linked_list_time(g, False, measurements) for g in graphs]
    weighted_times = [test_linked_list_time(g, True, measurements) for g in graphs]
    forest_times = [test_forest_time(g, measurements) for g in graphs]
    plt.plot(dimensions, unweighted_times, label="Linked List (unweighted)")
    plt.plot(dimensions, weighted_times, label="Linked List (weighted)")
    plt.plot(dimensions, forest_times, label="Forest (path compression)")
    plt.title(f"|E| = {edges_nodes_ratio}*|V|")
    plt.xlabel("|V|")
    plt.ylabel("Time (s)")
    plt.legend()
    plt.show()


def compare_wlist_vs_forest(edges_nodes_ratio, step=500, measurements=5):
    dimensions = [step * i for i in range(1, 11)]
    graphs = [graph.Graph(dim, edges_nodes_ratio * dim) for dim in dimensions]
    weighted_times = [test_linked_list_time(g, True, measurements) for g in graphs]
    forest_times = [test_forest_time(g, measurements) for g in graphs]
    plt.plot(dimensions, weighted_times, label="Linked List (unweighted)")
    plt.plot(dimensions, forest_times, label="Forest (path compression)")
    plt.title(f"|E| = {edges_nodes_ratio}*|V|")
    plt.xlabel("|V|")
    plt.ylabel("Time (s)")
    plt.legend()
    plt.show()
