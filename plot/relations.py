from collections import defaultdict, deque
import matplotlib.pyplot as plt
import networkx as nx

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.capacity = {}

    def add_edge(self, u, v, cap):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.capacity[(u, v)] = cap
        self.capacity[(v, u)] = 0

    def bfs(self, s, t, parent):
        visited = [False] * self.V
        queue = deque([s])
        visited[s] = True

        while queue:
            u = queue.popleft()
            for v in self.graph[u]:
                if not visited[v] and self.capacity[(u, v)] > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == t:
                        return True
        return False

    def edmonds_karp_relations(self, source, sink):
        parent = [-1] * self.V
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float('Inf')
            s = sink
            while s != source:
                path_flow = min(path_flow, self.capacity[(parent[s], s)])
                s = parent[s]
            max_flow += path_flow
            v = sink
            while v != source:
                u = parent[v]
                self.capacity[(u, v)] -= path_flow
                self.capacity[(v, u)] += path_flow
                v = parent[v]
        return max_flow


def build_graph(people, relations):
    n = len(people)
    source = n
    sink = n + 1
    g = Graph(n + 2)

    front_ids = []
    back_ids = []

    for i, person in enumerate(people):
        if person['hands'] == 'front':
            front_ids.append(i)
            g.add_edge(source, i, 1)
        elif person['hands'] == 'back':
            back_ids.append(i)
            g.add_edge(i, sink, 1)

    for u, v in relations:
        if people[u]['hands'] == 'front' and people[v]['hands'] == 'back':
            g.add_edge(u, v, 1)
        elif people[u]['hands'] == 'back' and people[v]['hands'] == 'front':
            g.add_edge(v, u, 1)

    return g, source, sink, front_ids, back_ids


def draw_graph(people, relations, front_ids, back_ids):
    B = nx.Graph()
    B.add_nodes_from(front_ids, bipartite=0, color='red')
    B.add_nodes_from(back_ids, bipartite=1, color='blue')

    for u, v in relations:
        if people[u]['hands'] == 'front' and people[v]['hands'] == 'back':
            B.add_edge(u, v)
        elif people[u]['hands'] == 'back' and people[v]['hands'] == 'front':
            B.add_edge(v, u)

    pos = {}
    pos.update((node, (1, index)) for index, node in enumerate(front_ids))
    pos.update((node, (2, index)) for index, node in enumerate(back_ids))

    color_map = ['red' if node in front_ids else 'blue' for node in B]

    plt.figure(figsize=(10, 6))
    nx.draw(B, pos, node_color=color_map, with_labels=True, node_size=500, font_color='white')
    plt.title('Bipartite Graph')
    plt.show()


def read_input():
    n = int(input("Enter the number of porters: "))
    people = []
    for i in range(n):
        hands = input(f"Porter {i} (front/back): ")
        people.append({'id': i, 'hands': hands})

    relations = []
    print("Enter relationship (porter1 porter2), enter 'end' to finish:")
    while True:
        rel = input()
        if rel.lower() == 'end':
            break
        u, v = map(int, rel.split())
        relations.append((u, v))

    return people, relations