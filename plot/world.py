import random
import matplotlib.pyplot as plt
from point import LandPoint, BasePoint


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

    def set_fence_points(self, points: list[BasePoint]) -> None:
        self.fence_points = points

    def count_points(self):
        if not self.fence_points:
            return 0, 0

        points_on_fence = set(self.fence_points)
        points_inside_fence = set(self.land_points) - points_on_fence

        return len(points_on_fence), len(points_inside_fence)


class WorldVisualizer:
    @staticmethod
    def plot_world(world: World):
        x = [point.x for point in world.land_points]
        y = [point.y for point in world.land_points]
        plt.scatter(x, y)
        plt.show()

    @staticmethod
    def plot_fence(world: World):
        if not world.fence_points:
            print("Fence points are not set.")
            return

        x = [point.x for point in world.fence_points]
        y = [point.y for point in world.fence_points]

        first_x = world.fence_points[0].x
        first_y = world.fence_points[0].y
        x.append(first_x)
        y.append(first_y)

        plt.plot(x, y)
        plt.show()
