import random
from collections.abc import Generator, Iterable

import matplotlib.pyplot as plt
import networkx as nx
from point import LandPoint


class World:
    def __init__(
        self,
        width: float,
        height: float,
        land_points: list[LandPoint] | None = None,
    ) -> None:
        self.width = width
        self.height = height
        self.land_points = land_points or []
        self.fence_points = None


class WorldGenerator:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def generate_land_points(self, number_of_points: int) -> list[LandPoint]:
        """
        Generate a list of random land points.

        Args:
            number_of_points (int): The number of land points to generate.

        Returns:
            list[LandPoint]: A list of randomly generated land points.
        """

        return [
            LandPoint(x=random.uniform(0, self.width), y=random.uniform(0, self.height))
            for _ in range(number_of_points)
        ]

    def generate_world(self, number_of_points: int) -> World:
        """
        Generate a world with random land points.

        Args:
            number_of_points (int): The number of land points to generate.

        Returns:
            World: A world with randomly generated land points.
        """

        return World(
            width=self.width,
            height=self.height,
            land_points=self.generate_land_points(number_of_points=number_of_points),
        )


class WorldVisualizer:
    @staticmethod
    def plot_world(world: World):
        x = [point.x for point in world.land_points]
        y = [point.y for point in world.land_points]
        plt.scatter(x, y)
        plt.show()

    @staticmethod
    def plot_fence(world: World):
        x = [point.x for point in world.fence_points]
        y = [point.y for point in world.fence_points]

        # First point added to the end to close the loop
        first_x = world.fence_points[0].x
        first_y = world.fence_points[0].y
        x.append(first_x)
        y.append(first_y)

        plt.plot(x, y)
        plt.show()


class WorldNetwork:
    def __init__(self, world: World) -> None:
        self.world = world
        self.edges = []


class NetworkEdge:
    def __init__(self, points: Iterable[LandPoint], capacity: float) -> None:
        if len(points) != 2:
            raise ValueError("An edge must have exactly two points.")
        self.points = set(points)
        self.capacity = capacity


class FlowNetwork(nx.DiGraph):
    pass

class NetworkGenerator:
    def __init__(self, world: World) -> None:
        self.world = world

    def _closest_points(self, point: LandPoint, radius: float) -> Generator[LandPoint]:
        """
        Find the closest points to a given point within a given radius.

        Args:
            point (LandPoint): The point to find the closest points to.
            radius (float): The radius within which to search for points.

        Returns:
            Generator[LandPoint]: The closest points to the given point
            within the given radius.
        """

        return (
            other_point
            for other_point in self.world.land_points
            if point != other_point
            and (point.x - other_point.x) ** 2 + (point.y - other_point.y) ** 2
            <= radius**2
        )

    def _generate_edges(
        self,
        radius: float,
        ratio_to_fill: float,
        capacity_range: range,
    ) -> None:
        """
        Generate edges between points within a given radius.

        Args:
            radius (float): The radius within which to generate edges.
            ratio_to_fill (float): The ratio of the network to fill with edges.
            capacity_range (range): The range of capacities for the edges.
        """

        edges = []

        points = self.world.land_points

        # Step 1: Ensure initial strong connectivity using a circular connection
        for i in range(len(points)):
            next_point = points[(i + 1) % len(points)]
            capacity = random.choice(capacity_range)
            edges.append(NetworkEdge(points=(points[i], next_point), capacity=capacity))

        # Step 2: Add additional edges to meet the ratio_to_fill
        for point in points:
            closest_points = list(self._closest_points(point=point, radius=radius))
            number_of_edges = max(1, int(len(closest_points) * ratio_to_fill))
            for other_point in random.sample(closest_points, number_of_edges):
                capacity = random.choice(capacity_range)
                edges.append(NetworkEdge(points=(point, other_point), capacity=capacity))

        return edges

    def generate_network(
        self,
        radius: float,
        ratio_to_fill: float,
        capacity_range: range,
    ) -> FlowNetwork:
        """
        Generate a flow network based on the world.

        Args:
            radius (float): The radius within which to generate edges.
            ratio_to_fill (float): The ratio of the network to fill with edges.
            capacity_range (range): The range of capacities for the edges.

        Returns:
            FlowNetwork: The generated flow network.
        """
        if radius <= 0:
            raise ValueError("The radius must be greater than 0.")

        if not 0 < ratio_to_fill <= 1:
            raise ValueError("The ratio to fill must be between 0 and 1.")

        if not capacity_range:
            raise ValueError("The capacity range must not be empty.")

        network = FlowNetwork()

        edges = self._generate_edges(
            radius=radius,
            ratio_to_fill=ratio_to_fill,
            capacity_range=capacity_range,
        )
        network.add_edges_from(
            (*edge.points, {"capacity": edge.capacity}) for edge in edges
        )

        return network


class NetworkVisualizer:
    @staticmethod
    def plot_network(network: FlowNetwork):
        pos = {node: (node.x, node.y) for node in network.nodes()}

        nx.draw_networkx_nodes(network, pos)
        nx.draw_networkx_edges(network, pos, edgelist=network.edges())

        edge_labels = {(u, v): d["capacity"] for u, v, d in network.edges(data=True)}
        nx.draw_networkx_edge_labels(network, pos, edge_labels=edge_labels)

        plt.show()
