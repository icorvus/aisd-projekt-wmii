import math
from functools import cmp_to_key
from point import BasePoint


class GrahamScan:
    def find_convex_hull(self, points: list[BasePoint]) -> list[BasePoint]:
        self.p0 = min(points, key=lambda point: (point.y, point.x))
        sorted_points = sorted(points, key=cmp_to_key(self._by_polar_angle))
        stack = []

        for point in sorted_points:
            while len(stack) > 1 and self._is_clockwise(stack[-2], stack[-1], point):
                stack.pop()

            stack.append(point)

        return stack

    def _is_clockwise(self, p1: BasePoint, p2: BasePoint, p3: BasePoint) -> bool:
        return (p2.x - p1.x) * (p3.y - p1.y) - (p3.x - p1.x) * (p2.y - p1.y) < 0

    def _by_polar_angle(self, p1: BasePoint, p2: BasePoint) -> float:
        angle_a = math.atan2(p1.y - self.p0.y, p1.x - self.p0.x)
        angle_b = math.atan2(p2.y - self.p0.y, p2.x - self.p0.x)

        if angle_a == angle_b:
            return self._distance_between(self.p0, p1) - self._distance_between(
                self.p0,
                p2,
            )

        return angle_a - angle_b

    @staticmethod
    def _distance_between(p1: BasePoint, p2: BasePoint) -> float:
        return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


class ConvexHullSearcher:
    def __init__(self, points: list[BasePoint]) -> None:
        self.points = points
        self.strategy = GrahamScan()

    def find_convex_hull(self) -> list[BasePoint]:
        return self.strategy.find_convex_hull(self.points)
