'''
Algorithms Specialization. Stanford University.
Course 2. Project 1: Kosaraju's Two-Pass Algorithm
Author: Luis Hernández
GitHub: luishc1618
Date: 3/20/2023
'''

# Imports.
import dfs
import helpers

# Read the .txt with the graph data.
path = r'C:\Users\luish\Desktop\Algortihms (2020)\Course 2\week 1'

test = 0  # Determines the test file used to test the program (if test = 5 the file test_5.txt is used).
if test != 0:
    with open(path + '\\' + 'test' + '\\' + 'test_' + str(test) + '.txt') as f:
        edges = f.readlines()
else:
    with open(path + '\\' + 'data' + '\\' + 'data.txt') as f:
        edges = f.readlines()

# Filter numeric data from the list of edges.
edges = helpers.graph_edges_computation(edges)
reversed_edges = helpers.reversal_of_graph_edges(edges)

# The edges are sorted in increasing order.
edges = helpers.sorted_edges(edges)
reversed_edges = helpers.sorted_edges(reversed_edges)

# Creation of the Adjacency List for the original graph.
graph = helpers.compute_adjacency_list(edges)

# Creation of the Adjacency List for the reversed graph.
graph_reversed = helpers.compute_adjacency_list(reversed_edges)

# Compute the number of nodes in the graph.
num_nodes = max(max(graph.keys()), max(graph_reversed.keys()))

# Run DFS-Loop on the reversed graph.
finishing_times = dfs.dfs_first_pass(num_nodes, graph_reversed)

# Run DFS-Loop on the original graph.
leaders = dfs.dfs_second_pass(num_nodes, graph, finishing_times)

# The sizes of the top SCCs are computed.
connected_components = helpers.size_of_ssc(leaders, 5)

# The final result is printed.
print(connected_components)
