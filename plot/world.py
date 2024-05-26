import random

import matplotlib.pyplot as plt
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
