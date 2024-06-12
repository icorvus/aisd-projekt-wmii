import numpy as np


class EdmondsKarp:
    def __init__(self, capacity_matrix):
        self.size = len(capacity_matrix)
        self.capacity = capacity_matrix
        self.flow = np.zeros((self.size, self.size), dtype=int)

    def bfs(self, source, sink, parent):
        visited = [False] * self.size
        queue = [source]
        visited[source] = True

        while queue:
            u = queue.pop(0)

            for v in range(self.size):
                if not visited[v] and self.capacity[u][v] - self.flow[u][v] > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u

        return visited[sink]

    def edmonds_karp(self, source, sink):
        parent = [-1] * self.size
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float('Inf')
            s = sink

            while s != source:
                path_flow = min(path_flow, self.capacity[parent[s]][s] - self.flow[parent[s]][s])
                s = parent[s]

            v = sink
            while v != source:
                u = parent[v]
                self.flow[u][v] += path_flow
                self.flow[v][u] -= path_flow
                v = parent[v]

            max_flow += path_flow

        return max_flow