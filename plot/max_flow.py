import math
from functools import cmp_to_key

from point import BasePoint, LandPoint
from world import FlowNetwork

# class EndomndsKarp:
#     def _bfs(self, network: FlowNetwork, source: LandPoint, sink: LandPoint):
#         """
#         Perform a breadth-first search on a network.

#         Args:
#             network (FlowNetwork): The network.
#             source (LandPoint): The source of the flow.
#             sink (LandPoint): The sink of the flow.

#         Returns:
#             path: The path from the source to the sink.
#         """

#         visited = {source}
#         queue = [[source]]

#         while queue:
#             path = queue.pop(0)
#             node = path[-1]

#             if node == sink:
#                 return path

#             for neighbor in network.neighbors(node):
#                 if neighbor not in visited:
#                     visited.add(neighbor)
#                     queue.append(path + [neighbor])
        

#     def find_max_flow(self, network: FlowNetwork, source: LandPoint, sink: LandPoint):
#         """
#         Find the max flow in a network.

#         Args:
#             network (FlowNetwork): The network.
#             source (LandPoint): The source of the flow.
#             sink (LandPoint): The sink of the flow.

#         Returns:
#             edges: The edges of the max flow.
#             value: The value of the max flow.
#         """

#         max_flow = 0

#         while True:
#             path = self._bfs(network, source, sink)

#             if not path:
#                 break

#             flow = min(network.get_capacity(u, v) for u, v in zip(path, path[1:]))

#             for u, v in zip(path, path[1:]):
#                 network[u][v]["capacity"] -= flow
#                 network[v][u]["capacity"] += flow
                
#             max_flow += flow

#         return network.edges, max_flow


# import networkx as nx
# from collections import deque

# class EdmondsKarp:
#     def __init__(self) -> None:
#         pass

#     def bfs(self, residual_graph, source, sink, parent):
#         visited = {node: False for node in residual_graph}
#         queue = deque([source])
#         visited[source] = True

#         while queue:
#             print(sink, source)
#             u = queue.popleft()

#             for v in residual_graph[u]:
#                 if not visited[v] and residual_graph[u][v]['capacity'] - residual_graph[u][v]['flow'] > 0:
#                     queue.append(v)
#                     print(queue)
#                     visited[v] = True
#                     parent[v] = u
#                     if v == sink:
#                         print("FOUND!")
#                         return True

#         return False

#     def find_max_flow(self, network: FlowNetwork, source: LandPoint, sink: LandPoint):
#         residual_graph = network.copy()
#         for u, v in residual_graph.edges:
#             residual_graph[u][v]['flow'] = 0

#         max_flow = 0
#         parent = {}

#         while self.bfs(residual_graph, source, sink, parent):
#             path_flow = float('Inf')
#             s = sink

#             while s != source:
#                 path_flow = min(path_flow, residual_graph[parent[s]][s]['capacity'] - residual_graph[parent[s]][s]['flow'])
#                 s = parent[s]

#             v = sink
#             while v != source:
#                 u = parent[v]
#                 residual_graph[u][v]['flow'] += path_flow
#                 residual_graph[v][u]['flow'] -= path_flow
#                 v = parent[v]

#             max_flow += path_flow

#         edges = [(u, v, residual_graph[u][v]['flow']) for u, v in residual_graph.edges if residual_graph[u][v]['flow'] > 0]
#         return edges, max_flow


class FordFulkerson:
    def __init__(self):
        self.visited = set()

    def find_max_flow(self, network: FlowNetwork, source: LandPoint, sink: LandPoint):
        """
        Find the max flow in the network using the Ford-Fulkerson algorithm.

        Args:
            network (FlowNetwork): The flow network.
            source (LandPoint): The source of the flow.
            sink (LandPoint): The sink of the flow.

        Returns:
            edges: The edges of the max flow.
            value: The value of the max flow.
        """
        max_flow = 0
        residual_network = network.copy()

        while self._bfs(residual_network, source, sink):
            path_flow = float('Inf')
            s = sink

            while s != source:
                path_flow = min(path_flow, residual_network[self.parent[s]][s]['capacity'])
                s = self.parent[s]

            max_flow += path_flow

            v = sink
            while v != source:
                u = self.parent[v]
                residual_network[u][v]['capacity'] -= path_flow
                if residual_network[u][v]['capacity'] == 0:
                    residual_network.remove_edge(u, v)
                if residual_network.has_edge(v, u):
                    residual_network[v][u]['capacity'] += path_flow
                else:
                    residual_network.add_edge(v, u, capacity=path_flow)
                v = self.parent[v]

        return residual_network.edges(data=True), max_flow

    def _bfs(self, residual_network, source, sink):
        """
        Breadth-First Search to find an augmenting path in the residual network.

        Args:
            residual_network (FlowNetwork): The residual network.
            source (LandPoint): The source of the flow.
            sink (LandPoint): The sink of the flow.

        Returns:
            bool: True if there is an augmenting path, False otherwise.
        """
        self.parent = {}
        visited = set()
        queue = [source]
        visited.add(source)

        while queue:
            u = queue.pop(0)

            for v in residual_network.neighbors(u):
                if v not in visited and residual_network[u][v]['capacity'] > 0:
                    queue.append(v)
                    visited.add(v)
                    self.parent[v] = u
                    if v == sink:
                        return True

        return False
        

class MaxFlowFinder:
    def __init__(self, network: FlowNetwork) -> None:
        self.network = network
        self.strategy = FordFulkerson()

    def find_max_flow(self, source: LandPoint, sink: LandPoint):
        """
        Find the max flow in a network.

        Args:
            source (LandPoint): The source of the flow.
            sink (LandPoint): The sink of the flow.

        Returns:
            edges: The edges of the max flow.
            value: The value of the max flow.
        """

        return self.strategy.find_max_flow(self.network, source, sink)
