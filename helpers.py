"""
Algorithms Specialization. Stanford University.
Course 2. Project 1: Kosaraju's Two-Pass Algorithm
Author: Luis Hernández
GitHub: luishc1618
Date: 3/20/2023
"""

import itertools
from collections import Counter


def graph_edges_computation(edges):
    """Returns the graph edges as a list of tuples.

    :param edges: list of edges, e.g. ['1 2\n', '2 1\n', '2 3\n'] -> Edges from 1 to 2, from 2 to 1 and from 2 to 3.
    :return: formatted_edges: list of tuples, in which each tuple represents an edge, e.g. [(1,2), (2,3), ... ].
    """

    num_edges = int(len(edges))
    formatted_edges = [None]*num_edges
    i = 0
    for element in edges:
        formatted_edges[i] = (int(element.split()[0]), int(element.split()[1]))
        i += 1

    return formatted_edges


def reversal_of_graph_edges(edges):
    """Returns the graph edges in reverse order.

    :param edges: list of tuples, in which each tuple represents an edge, e.g. [(1,2), (2,3), ... ].
    :return: reversed_edges: list of reversed edges, e.g. [(2,1), (3,2), ...].
    """
    reversed_edges = [tup[::-1] for tup in edges]
    reversed_edges = sorted(reversed_edges, key=lambda tup: tup[0])

    return reversed_edges


def sorted_edges(edges):
    """Returns the graph edges in increasing order according to the edges tails,
     e.g. [(3,2), (1,4), (2,5), ...] --> [(1,4), (2,5), (3,2), ...]

     :param edges: list of tuples, in which each tuple represents an edge, e.g. [(1,2), (2,3), ... ].
     :return edges: list of sorted edges.
    """

    edges = sorted(edges, key=lambda tup: tup[0])

    return edges


def compute_adjacency_list(edges):
    """Returns the graph adjacency list in the form of a dictionary. Each Key:Value pair represents a node (the Key) with
    its corresponding list of neighbors (the Value).
    Example: {1:[2,5,7], 2:[1,7], 3:[4,2,8,7], ... }

    :param edges: list of tuples, in which each tuple represents an edge, e.g. [(1,2), (2,3), ... ]
    :return adjacency_dict: graph adjacency list in the form of a dictionary.
    """

    adjacency_list = itertools.groupby(edges, lambda x: x[0])

    adjacency_dict = {}
    for key, val in adjacency_list:
        adjacency_dict[key] = [head[1] for head in val]

    return adjacency_dict


def size_of_ssc(leaders, number_of_scc):
    """Returns a list with the size of the top largest Strongly Connected Components.
    The number of top SCCs is determined with number_of_scc.

    :param leaders: dict that stores from which node the current node was discovered
    e.g. {Node 17: 4} -> Node 17 was discovered from Node 4.
    :param number_of_scc: defines the number of top SCCs the function returns.
    e.g. if number_of_scc is 5 the function returns the 5 largest SCCs.
    :return: scc_sizes[0:number_of_scc]: list of sizes with the top largest SCCs according to number_of_scc.
    """

    leaders = list(leaders.values())
    scc_sizes = Counter(leaders)
    scc_sizes = sorted(scc_sizes.values(), reverse=True)
    if len(scc_sizes) <= number_of_scc:
        return scc_sizes
    else:
        return scc_sizes[0:number_of_scc]
