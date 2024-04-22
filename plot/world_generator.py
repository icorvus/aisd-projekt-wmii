import random

from point import LandPoint


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
            for i in range(number_of_points)
        ]
