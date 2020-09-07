# -*- coding: utf-8 -*-


class Graph:
    """
    a directed graph using adjacency list representation
    """

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = {}
        self.path = []

        # function to add an edge to graph

    def add_edge(self, u, v):
        """
        to add an edge to graph
        :param u: start point
        :param v: end point
        """
        if u in self.graph.keys():
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    def search(self, v, visited):
        # Mark the current node as visited
        # and print it
        visited[v] = True
        self.path.append(v)

        # Recur for all the vertices
        # adjacent to this vertex
        for i in self.graph[v]:
            if not visited[i]:
                self.search(i, visited)

    # recursive DFSUtil()
    def visit(self, v):
        # Mark all the vertices as not visited
        # max of keys in a dict
        visited = [False] * (max(self.graph) + 1)

        # Call the recursive helper function
        # to print DFS traversal
        self.search(v, visited)
