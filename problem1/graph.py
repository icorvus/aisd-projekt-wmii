import matplotlib.pyplot as plt
import heapq
import math
from graham import Graham, Point
import user


class Graph:
    def __init__(self, points, edges):
        self.points = points
        self.edges = edges
        self.graph = self._build_graph()

    def _build_graph(self):
        graph = {point: [] for point in self.points}
        for edge in self.edges:
            p1, p2 = self.points[edge[0] - 1], self.points[edge[1] - 1]
            distance = self._distance(p1, p2)
            graph[p1].append((p2, distance))
            graph[p2].append((p1, distance))  # Assuming undirected graph
        return graph

    def _distance(self, point1, point2):
        return ((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2) ** 0.5

    def dijkstra(self, start_point, end_point):
        start = self.points[start_point - 1]
        end = self.points[end_point - 1]
        pq = [(0, start)]
        dist = {point: float('inf') for point in self.points}
        dist[start] = 0
        prev = {point: None for point in self.points}
        visited = set()

        while pq:
            current_dist, current_point = heapq.heappop(pq)
            if current_point in visited:
                continue
            visited.add(current_point)

            if current_point == end:
                break

            for neighbor, weight in self.graph[current_point]:
                distance = current_dist + weight
                if distance < dist[neighbor]:
                    dist[neighbor] = distance
                    prev[neighbor] = current_point
                    heapq.heappush(pq, (distance, neighbor))

        path = []
        step = end
        while step is not None:
            path.append(step)
            step = prev[step]
        path.reverse()

        return dist[end], path

    def plotNetwork(self, graham):
        hull_indices = graham.convexHull()
        if not hull_indices:
            return

        hull_points = [graham.points[i] for i in hull_indices]

        # Dodaj pierwszy punkt na koniec listy, aby zamknąć otoczkę
        hull_points.append(hull_points[0])

        # Wykres punktów
        x_points = [point.x for point in graham.points]
        y_points = [point.y for point in graham.points]
        plt.scatter(x_points, y_points, label='Punkty')

        # Wykres otoczki wypukłej
        x_hull = [point.x for point in hull_points]
        y_hull = [point.y for point in hull_points]
        plt.plot(x_hull, y_hull, 'r-', label='Otoczka wypukła')

        # Wykres sieci przepływowej
        for edge in self.edges:
            p1 = graham.points[edge[0] - 1]
            p2 = graham.points[edge[1] - 1]
            plt.plot([p1.x, p2.x], [p1.y, p2.y], 'b--')

        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Sieć przepływowa')
        plt.legend()
        plt.savefig("plot_network.png")
        plt.close()

    def plotNetworkWithPath(self, graham, path):
        hull_indices = graham.convexHull()
        if not hull_indices:
            return

        hull_points = [graham.points[i] for i in hull_indices]

        # Dodaj pierwszy punkt na koniec listy, aby zamknąć otoczkę
        hull_points.append(hull_points[0])

        # Wykres punktów
        x_points = [point.x for point in graham.points]
        y_points = [point.y for point in graham.points]
        plt.scatter(x_points, y_points, label='Punkty')

        # Wykres otoczki wypukłej
        x_hull = [point.x for point in hull_points]
        y_hull = [point.y for point in hull_points]
        plt.plot(x_hull, y_hull, 'r-', label='Otoczka wypukła')

        # Wykres sieci przepływowej z wagami krawędzi
        for edge in self.edges:
            p1 = graham.points[edge[0] - 1]
            p2 = graham.points[edge[1] - 1]
            plt.plot([p1.x, p2.x], [p1.y, p2.y], 'b--')
            mid_x, mid_y = (p1.x + p2.x) / 2, (p1.y + p2.y) / 2
            plt.text(mid_x, mid_y, f'{self._distance(p1, p2):.2f}', color='black', fontsize=8, ha='center')

        # Wykres najkrótszej ścieżki
        for i in range(len(path) - 1):
            p1, p2 = path[i], path[i + 1]
            plt.plot([p1.x, p2.x], [p1.y, p2.y], 'g-', linewidth=2)

        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Otoczka, graf oraz wyznaczona najkrotsza droga')
        plt.legend()
        plt.savefig("plot_network_with_path.png")
        plt.close()

    def updatePointsAndGraph(self, points, edges):
        self.points = points
        self.edges = edges
        self.graph = self._build_graph()