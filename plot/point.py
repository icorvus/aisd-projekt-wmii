class BasePoint:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.x}, {self.y})"


class LandPoint(BasePoint):
    pass
