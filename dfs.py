"""
Algorithms Specialization. Stanford University.
Course 2. Project 1: Kosaraju's Two-Pass Algorithm
Author: Luis Hernández
GitHub: luishc1618
Date: 3/20/2023
"""

from collections import deque

time = 0
source = 0


def nodes_in_correct_order(finishing_times):
    """Returns the graph nodes sorted in decreasing order of finishing times.
    
    :param finishing_times: dict that stores the discovery finishing times for each node 
    (e.g. {24: 4} -> Node 24 was the 4th node discovered).
    :return ordered_nodes: list containing the nodes in the required order.
    """

    nodes = list(finishing_times.keys())
    times = list(finishing_times.values())
    ordered_nodes = [n for (t, n) in sorted(zip(times, nodes), key=lambda pair: pair[0], reverse=True)]

    return ordered_nodes


def depth_first_search_first_pass(node, explored_nodes, graph, source_nodes, finishing_times):
    """Iterative version of Depth-First Search used for Kosaraju's Two Pass Algorithm.
    
    :param node: node to be explored.
    :param explored_nodes: dictionary that indicates which nodes are explored (e.g. {5: True} -> Node 5 is explored).
    :param graph: dictionary that acts as the graph adjacency list.
    :param source_nodes: list of nodes that have at least one out-edge.
    :param finishing_times: dict that stores the discovery finishing times for each node
    (e.g. {24: 4} -> Node 24 was the 4th node discovered).
    :return: None.
    """

    global time
    global source

    # Create the stack for DFS and push current node into it.
    stack = deque()
    stack.append(node)
    # Create a set of seen nodes. A set is used to achieve O(1) time complexity when using the "not in" operator.
    seen_nodes = set()
    # Loop till stack is empty.
    while stack:
        node = stack.pop()
        # The DFS procedure continues if this is the first time we have seen the node.
        if node not in seen_nodes:
            explored_nodes[node] = True
            seen_nodes.add(node)
            # The node has to be re-appended to the stack in order to compute the finishing times.
            # This trick ensures that when popping the node for second time the node has to be finished.
            stack.append(node)
            # The node is ignored if it doesn't have at least one out-going edge.
            if node in source_nodes:
                neighbors = graph[node]
                for neighbor in neighbors:
                    if explored_nodes[neighbor] is False:
                        stack.append(neighbor)
        # If the node has already been seen the node is finished.
        else:
            if finishing_times[node] is None:
                time += 1
                finishing_times[node] = time

    return None


def dfs_first_pass(num_nodes, graph):
    """Returns the finishing times for the Kosaraju's Two Pass Algorithm.
    
    :param num_nodes: total number of nodes of the graph.
    :param graph: dictionary that acts as the graph adjacency list.
    :return finishing_times: dict that stores the discovery finishing times for each node
    (e.g. {24: 4} -> Node 24 was the 4th node discovered).
    """

    global time
    global source

    total_nodes = range(1, num_nodes + 1)

    # A dictionary is used to remember which nodes have been explored.
    explored_nodes = {key: value for (key, value) in zip(total_nodes, [False] * num_nodes)}
    # A dictionary is used to store the discovery finishing times of each node.
    finishing_times = {key: value for (key, value) in zip(total_nodes, [None] * num_nodes)}
    # Source nodes are computed to avoid KeyError messages when trying to access graph[node] when...
    # node doesn't have outgoing edges.
    # A set is used to achieve O(1) time complexity when using the "in" operator.
    source_nodes = set(list(graph.keys()))
    # Main DFS Loop.
    for node in range(num_nodes, 0, -1):
        if explored_nodes[node] is False:
            depth_first_search_first_pass(node, explored_nodes, graph, source_nodes, finishing_times)

    return finishing_times


def depth_first_search_second_pass(node, explored_nodes, leader_nodes, graph, source_nodes):
    """Iterative version of Depth-First Search used for Kosaraju's Two Pass Algorithm.

     :param node: node to be explored.
     :param explored_nodes: dictionary that indicates which nodes are explored (e.g. {5: True} -> Node 5 is explored).
     :param leader_nodes: dict that stores from which node the current node was discovered
     (e.g. {Node 17: 4} -> Node 17 was discovered from Node 4).
     :param graph: dictionary that acts as the graph adjacency list.
     :param source_nodes: list of nodes that have at least one out-edge.
     :return: None.
     """

    global time
    global source

    # Create the stack for DFS and push current node into it.
    stack = deque()
    stack.append(node)
    # Loop till stack is empty.
    while stack:
        node = stack.pop()
        if explored_nodes[node] is False:
            explored_nodes[node] = True
            leader_nodes[node] = source
            if node in source_nodes:
                neighbors = graph[node]
                for neighbor in neighbors:
                    if explored_nodes[neighbor] is False:
                        stack.append(neighbor)

    return None


def dfs_second_pass(num_nodes, graph, finishing_times):
    """Returns the leaders of all nodes for the Kosaraju's Two Pass Algorithm.

    :param num_nodes: total number of nodes of the graph.
    :param graph: dictionary that acts as the graph adjacency list.
    :param finishing_times: dict that stores the discovery finishing times for each node.
    :return leader_nodes: dict that stores from which node the current node was discovered
    (e.g. {Node 17: 4} -> Node 17 was discovered from Node 4).
    """

    global time
    global source

    total_nodes = range(1, num_nodes + 1)

    # A dictionary is used to remember which nodes have been explored.
    explored_nodes = {key: value for (key, value) in zip(total_nodes, [False] * num_nodes)}
    # A dictionary is used to store the leaders of each node.
    leader_nodes = {key: value for (key, value) in zip(total_nodes, [None] * num_nodes)}
    # Source nodes are computed to avoid KeyError messages when trying to access graph[node] when...
    # node doesn't have outgoing edges.
    # A set is used to achieve O(1) time complexity when using the "in" operator.
    source_nodes = set(list(graph.keys()))
    # The nodes are sorted in accordance with the finishing time.
    ordered_nodes = nodes_in_correct_order(finishing_times)
    # Main DFS Loop.
    for node in ordered_nodes:
        if explored_nodes[node] is False:
            source = node
            depth_first_search_second_pass(node, explored_nodes, leader_nodes, graph, source_nodes)

    return leader_nodes
